import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int N;
	static int M;
	static int D;
	static int[][] arr;
	static int answer = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		D = sc.nextInt();

		arr = new int[N][M];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				arr[i][j] = sc.nextInt();
		comb(0, 0, new boolean[M]);
		System.out.println(answer);
		sc.close();
	}

	static void comb(int start, int depth, boolean[] selected) {
		if (depth == 3) {
			int[][] copy = new int[N][M];
			for (int i = 0; i < N; i++)
				copy[i] = arr[i].clone();

			int cur = game(copy, selected);
			answer = Math.max(answer, cur);
			return;
		}
		for (int i = start; i < M; i++) {
			selected[i] = true;
			comb(i + 1, depth + 1, selected);
			selected[i] = false;
		}
	}

	static int game(int[][] copy, boolean[] selected) {
		int result = 0;
		int leftEnemy = 0;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				if (copy[i][j] == 1)
					leftEnemy++;

		while (leftEnemy > 0) {
			
			// 공격
			List<int[]> willAttack = new ArrayList<>();
			for (int i = 0; i < M; i++) {
				if (selected[i]) {
					int aX = -1, aY = -1, min_dis = Integer.MAX_VALUE;
					for (int y = 0; y < N; y++) {
						for (int x = 0; x < M; x++) {
							if (copy[y][x] == 1) {
								int dis = Math.abs(x - i) + Math.abs(y - N);
								if (dis > D)
									continue;
								if (dis < min_dis) {
									aX = x;
									aY = y;
									min_dis = dis;
								} else if (dis == min_dis) {
									if (x < aX) {
										aX = x;
										aY = y;
									}
								}
							}

						}
					}
					if (aX != -1 && aY != -1)
						willAttack.add(new int[] { aX, aY });
				}
			}

			for (int[] temp : willAttack) {
				int x = temp[0];
				int y = temp[1];
				if (copy[y][x] == 1) {
					result++;
					copy[y][x] = 0;
					leftEnemy--;
				}
			}

			// 적 내리기
			for (int j = 0; j < M; j++) {
				if (copy[N - 1][j] == 1) {
					copy[N - 1][j] = 0;
					leftEnemy--;
				}
			}
			for (int i = N - 1; i > 0; i--)
				for (int j = 0; j < M; j++)
					copy[i][j] = copy[i - 1][j];
			for (int j = 0; j < M; j++)
				copy[0][j] = 0;

		}
		return result;
	}
}