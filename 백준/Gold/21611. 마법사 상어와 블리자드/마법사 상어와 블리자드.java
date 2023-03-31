import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int N;
	static int[][] matrix;
//	static LinkedList<Integer> marble;
	static List<int[]> marblePos; // 0 -> (N/2,N/2-1), 1-> (N/2+1,N/2-1), ...
	static int[][] matrixPos; // matrixPos[N/2][N/2-1] = 0, matrixPos[N/2+1][N/2-1] = 1;
	static int[] marbleList;
	static int marbleSize;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();

		int[] dx1 = { -1, 0, 1, 0 };
		int[] dy1 = { 0, 1, 0, -1 };
		List<Integer> moveAmount = new ArrayList<>();
		for (int i = 1; i < N; i++) {
			moveAmount.add(i);
			moveAmount.add(i);
		}
		moveAmount.add(N - 1);
		int sx1 = N / 2;
		int sy1 = N / 2;
		int dIdx1 = 0;
		int marbleNum = 0;
		marblePos = new ArrayList<>();
		matrixPos = new int[N][N];

		for (int temp : moveAmount) {
			while (temp-- > 0) {
				sx1 += dx1[dIdx1];
				sy1 += dy1[dIdx1];
				marblePos.add(new int[] { sy1, sx1 });
				matrixPos[sy1][sx1] = marbleNum++;
			}
			dIdx1 = (dIdx1 + 1) % 4;
		}

		int M = sc.nextInt();
		matrix = new int[N][N];
//		marble = new LinkedList<>();
		marbleSize = N * N - 1;
		marbleList = new int[marbleSize];
		marbleNum = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				matrix[i][j] = sc.nextInt();

			}
		}
		for (int[] temp : marblePos) {
//			System.out.println(Arrays.toString(temp)+" "+matrix[temp[0]][temp[1]]);
//			marble.add(matrix[temp[0]][temp[1]]);
			marbleList[marbleNum++] = matrix[temp[0]][temp[1]];
		}

		int[] dx2 = { 0, 0, -1, 1 };
		int[] dy2 = { -1, 1, 0, 0 };
		int answer = 0;
		while (M-- > 0) {
			// 블리자드
			int dir = sc.nextInt() - 1;
			int distance = sc.nextInt();
			int sx2 = N / 2;
			int sy2 = N / 2;
			while (distance-- > 0) {
				sx2 += dx2[dir];
				sy2 += dy2[dir];
				int marbleIdx = matrixPos[sy2][sx2];
				marbleList[marbleIdx] = 0;
			}

			// 구슬 폭발
			while (true) {
				int cnt = 1;
				int cur = marbleList[0];
				boolean check = false;
				for (int i = 1; i < marbleSize; i++) {
					if (marbleList[i] == 0)
						continue;
					if (cur == marbleList[i]) {
						cnt++;
					} else {
						if (cnt >= 4) {
							check = true;
							int minus = 1;
							int temp = 0;
							while (temp < cnt) {
								if (marbleList[i - minus] == 0) {
									minus++;
									continue;
								}
								answer += marbleList[i - minus];
								marbleList[i - minus++] = 0;
								temp++;
							}
						}

						cnt = 1;
						cur = marbleList[i];
					}
				}

				if (cnt >= 4) {
					check = true;
					int minus = 1;
					int temp = 0;
					while (temp < cnt) {
						if (marbleList[marbleSize - minus] == 0) {
							minus++;
							continue;
						}
						answer += marbleList[marbleSize - minus];
						marbleList[marbleSize - minus++] = 0;
						temp++;
					}
				}
				if (!check)
					break;
			}

			// 0 제거
			int[] temp = new int[marbleSize];
			int idx = 0;
			for (int i = 0; i < marbleSize; i++) {
				if (marbleList[i] == 0)
					continue;
				temp[idx++] = marbleList[i];
			}
			marbleList = temp;

			// 배열 채우기
			int fillIdx = 0;
			temp = new int[marbleSize];
			int cnt = 1;
			int cur = marbleList[0];
			for (int i = 1; i < marbleSize; i++) {
				if (marbleList[i - 1] == 0)
					break;
				if (cur == marbleList[i]) {
					cnt++;
				} else {
					if (fillIdx == marbleSize)
						break;
					temp[fillIdx++] = cnt;
					temp[fillIdx++] = marbleList[i - 1];
					cur = marbleList[i];
					cnt = 1;
				}
			}
			marbleList = temp;
		}
		System.out.println(answer);
		sc.close();

	}
}