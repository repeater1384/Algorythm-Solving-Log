import java.util.Scanner;

public class Main {
	static int N, M, T;
	static int[][] arr;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		T = sc.nextInt();

		int airY = 0;
		arr = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				arr[i][j] = sc.nextInt();
				if (arr[i][j] == -1)
					airY = i;
			}

		}

		int[] di = { 0, 1, 0, -1 };
		int[] dj = { 1, 0, -1, 0 };
		while (T-- > 0) {
			// 확산
			int[][] temp = new int[N][M];
			temp[airY - 1][0] = temp[airY][0] = -1;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					int cur = arr[i][j];
					if (cur <= 0)
						continue;
					int cnt = 0;
					for (int k = 0; k < 4; k++) {
						int ni = i + di[k];
						int nj = j + dj[k];
						if (0 <= ni && ni < N && 0 <= nj && nj < M && arr[ni][nj] != -1) {
							temp[ni][nj] += cur / 5;
							cnt++;
						}
					}
					temp[i][j] += cur - (cur / 5) * cnt;
				}
			}
			arr = temp;

			// 위쪽 공기청정기
			int upAirY = airY - 1;
			for (int i = upAirY - 2; i >= 0; i--) {
				arr[i + 1][0] = arr[i][0];
			}
			for (int j = 0; j < M - 1; j++) {
				arr[0][j] = arr[0][j + 1];
			}
			for (int i = 0; i < upAirY; i++) {
				arr[i][M - 1] = arr[i + 1][M - 1];
			}
			for (int j = M - 1; j > 1; j--) {
				arr[upAirY][j] = arr[upAirY][j - 1];
			}
			arr[upAirY][1] = 0;

			// 아래쪽 공기청정기
			int downAirY = airY;
			for (int i = downAirY + 1; i < N - 1; i++) {
				arr[i][0] = arr[i + 1][0];
			}
			for (int j = 0; j < M - 1; j++) {
				arr[N - 1][j] = arr[N - 1][j + 1];
			}
			for (int i = N - 1; i >= downAirY + 1; i--) {
				arr[i][M - 1] = arr[i - 1][M - 1];
			}
			for (int j = M - 1; j > 1; j--) {
				arr[downAirY][j] = arr[downAirY][j - 1];
			}
			arr[downAirY][1] = 0;
		}

		int answer = 2;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				answer += arr[i][j];
		System.out.println(answer);
		sc.close();
	}

}