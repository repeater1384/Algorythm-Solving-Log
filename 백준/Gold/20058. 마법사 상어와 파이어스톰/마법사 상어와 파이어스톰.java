import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int N;
	static int[][] arr;
	static int[] di = { 1, 0, -1, 0 };
	static int[] dj = { 0, 1, 0, -1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		int Q = sc.nextInt();
		int size = 1 << N;
		arr = new int[size][size];
		for (int i = 0; i < size; i++)
			for (int j = 0; j < size; j++)
				arr[i][j] = sc.nextInt();

		while (Q-- > 0) {
			int L = sc.nextInt();
			rotate(N - L, 0, 0, size / 2);
			int[][] temp = new int[size][size];
			for (int i = 0; i < size; i++) {
				for (int j = 0; j < size; j++) {
					for (int k = 0; k < 4; k++) {
						int ni = i + di[k];
						int nj = j + dj[k];
						if (0 <= ni && ni < size && 0 <= nj && nj < size && arr[ni][nj] > 0)
							temp[i][j]++;
					}
				}
			}
			for (int i = 0; i < size; i++) {
				for (int j = 0; j < size; j++) {
					if (temp[i][j] < 3)
						arr[i][j] = Math.max(arr[i][j] - 1, 0);
				}
			}
		}
		int answer1 = 0;
		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++) {
				answer1 += arr[i][j];
			}
		}

		int answer2 = 0;
		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++) {
				if (arr[i][j] > 0) {
					int curCnt = 0;
					Queue<int[]> queue = new LinkedList<>();
					arr[i][j] = 0;
					queue.add(new int[] { i, j });
					while (!queue.isEmpty()) {
						int[] cur = queue.poll();
						int ci = cur[0];
						int cj = cur[1];
						curCnt++;
						for (int k = 0; k < 4; k++) {
							int ni = ci + di[k];
							int nj = cj + dj[k];
							if (0 <= ni && ni < size && 0 <= nj && nj < size && arr[ni][nj] > 0) {
								queue.add(new int[] { ni, nj });
								arr[ni][nj] = 0;
							}
						}
					}
					answer2 = Math.max(answer2, curCnt);
				}
			}
		}
		System.out.println(answer1);
		System.out.println(answer2);
		sc.close();
	}

	static void rotate(int depth, int x, int y, int size) {
		if (depth == 0) {
			size *= 2;
			int[][] temp = new int[size][size];
			for (int i = 0; i < size; i++) {
				for (int j = 0; j < size; j++) {
					temp[i][j] = arr[y + size - 1 - j][x + i];
				}
			}
			for (int i = 0; i < size; i++) {
				for (int j = 0; j < size; j++) {
					arr[y + i][x + j] = temp[i][j];
				}
			}
			return;
		}
		rotate(depth - 1, x, y, size / 2);
		rotate(depth - 1, x + size, y, size / 2);
		rotate(depth - 1, x, y + size, size / 2);
		rotate(depth - 1, x + size, y + size, size / 2);
	}
}