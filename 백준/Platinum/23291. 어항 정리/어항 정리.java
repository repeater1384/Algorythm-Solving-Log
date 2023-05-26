import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int N;
	static int K;
	static int[] arr;
	static LinkedList<Integer>[] mainMatrix;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		K = sc.nextInt();
		arr = new int[N];
		for (int i = 0; i < N; i++)
			arr[i] = sc.nextInt();

		int answer = 0;
		while(true) {
			answer++;
			addMil();
			settingMainMatrix();
			flip();
			pressNflipNpress();
			if(isOk()) {
				System.out.println(answer);
				break;
			}
		}
		sc.close();
	}

	static void flip() {

		if (N == 1)
			return;
		if (N <= 3) {
			mainMatrix[1].add(mainMatrix[0].poll());
			return;
		}
		if (N <= 5) {
			mainMatrix[1].add(mainMatrix[0].poll());
			mainMatrix[1].addFirst(mainMatrix[0].poll());
			return;
		}

		mainMatrix[1].add(mainMatrix[0].poll());
		mainMatrix[1].addFirst(mainMatrix[0].poll());
		while (true) {
			int height = 0;
			for (; mainMatrix[height + 1].size() > 0; height++)
				;
			int width = mainMatrix[height].size();
			if (height != 0 && mainMatrix[0].size() - width <= height)
				break;

//			System.out.println(height + " " + width);
			LinkedList<LinkedList<Integer>> temp = new LinkedList<>();
			for (int i = 0; i < width; i++) {
				temp.add(new LinkedList<>());
			}

			for (int i = 0; i < width; i++) {
				for (int j = 0; j <= height; j++) {
					temp.get(i).add(mainMatrix[j].poll());
				}
			}
//			for (int tempIdx = 0; tempIdx < width; tempIdx++) 
//				System.out.println("a" + temp.get(tempIdx));
			int idx = 1;
			while (!temp.isEmpty()) {
				LinkedList<Integer> cur = temp.pollLast();
				while (!cur.isEmpty()) {
					mainMatrix[idx].add(cur.poll());
				}
				idx++;
			}
//			for (int i = 9; i >= 0; i--) {
//				System.out.println(mainMatrix[i]);
//			}
//			System.out.println("----------");
		}

	}

	static void pressNflipNpress() {
		int[][] matrix = new int[50][50];
		for (int i = 0; i < 50; i++) {
			int j = 0;
			while (!mainMatrix[i].isEmpty()) {
				matrix[i][j++] = mainMatrix[i].poll();
			}
		}

		int[][] newMatrix = new int[50][50];
		for (int i = 0; i < 50; i++) {
			for (int j = 0; j < 50; j++)
				newMatrix[i][j] = matrix[i][j];
		}

		int[] dx = { 1, 0, -1, 0 };
		int[] dy = { 0, 1, 0, -1 };
		for (int i = 0; i < 50; i++) {
			for (int j = 0; j < 50; j++) {
				if (matrix[i][j] == 0)
					continue;
				for (int k = 0; k < 4; k++) {
					int ny = i + dy[k];
					int nx = j + dx[k];
					if (0 <= ny && ny < 50 && 0 <= nx && nx < 50 && matrix[ny][nx] != 0) {
						int div = Math.abs(matrix[i][j] - matrix[ny][nx]) / 5;
						if (matrix[i][j] > matrix[ny][nx]) {
							newMatrix[i][j] -= div;
						} else {
							newMatrix[i][j] += div;
						}
					}
				}
			}
		}

		int[] flatArr = new int[N];
		int idx = 0;
		for (int j = 0; j < 50; j++) {
			for (int i = 0; i < 50; i++) {
				if (newMatrix[i][j] == 0)
					continue;
				flatArr[idx++] = newMatrix[i][j];
			}
		}
		int flag = N / 4;

		int[][] step1 = new int[2][N / 2];
		for (int i = 0; i < N / 2; i++) {
			step1[0][i] = flatArr[i + N / 2];
			step1[1][i] = flatArr[N / 2 - i - 1];
		}

		int[][] step2 = new int[50][50];
		for (int i = 0; i < N / 4; i++) {
			step2[0][i] = step1[0][i + N / 4];
			step2[1][i] = step1[1][i + N / 4];
			step2[2][i] = step1[1][N / 4 - i - 1];
			step2[3][i] = step1[0][N / 4 - i - 1];
		}

		int[][] newMatrix2 = new int[50][50];
		for (int i = 0; i < 50; i++) {
			for (int j = 0; j < 50; j++)
				newMatrix2[i][j] = step2[i][j];
		}

		for (int i = 0; i < 50; i++) {
			for (int j = 0; j < 50; j++) {
				if (step2[i][j] == 0)
					continue;
				for (int k = 0; k < 4; k++) {
					int ny = i + dy[k];
					int nx = j + dx[k];
					if (0 <= ny && ny < 50 && 0 <= nx && nx < 50 && step2[ny][nx] != 0) {
						int div = Math.abs(step2[i][j] - step2[ny][nx]) / 5;
						if (step2[i][j] > step2[ny][nx]) {
							newMatrix2[i][j] -= div;
						} else {
							newMatrix2[i][j] += div;
						}
					}
				}
			}
		}

		int[] flatArr2 = new int[N];
		idx = 0;
		for (int j = 0; j < 50; j++) {
			for (int i = 0; i < 50; i++) {
				if (newMatrix2[i][j] == 0)
					continue;
				flatArr2[idx++] = newMatrix2[i][j];
			}
		}
		arr = flatArr2;
	}

	static void settingMainMatrix() {
		mainMatrix = new LinkedList[50];
		for (int i = 0; i < 50; i++)
			mainMatrix[i] = new LinkedList<>();
		for (int i = 0; i < N; i++)
			mainMatrix[0].add(arr[i]);
	}

	static void addMil() {
		int MinVal = Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			MinVal = Math.min(MinVal, arr[i]);
		}
		for (int i = 0; i < N; i++) {
			if (arr[i] == MinVal)
				arr[i]++;
		}
	}

	static boolean isOk() {
		int min = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;
		for (int i = 0; i < N; i++) {
			min = Math.min(min, arr[i]);
			max = Math.max(max, arr[i]);
		}
		
		return max - min <= K;
	}
}