import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[][] matrix = new int[N][N];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				matrix[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// a, i, j -> a모양으로 i,j위치에 배치 될수 있는 가짓수
		// 0 -> 가로 1 -> 세로 2 -> 대각선
		int[][][] dp = new int[3][N + 1][N + 1];
		dp[0][1][2] = 1;

		for (int i = 1; i <= N; i++) {
			for (int j = 3; j <= N; j++) {
				if (matrix[i - 1][j - 1] != 1) {
					dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1];
					dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j];
				}
				if (i - 2 >= 0 && matrix[i - 1][j - 1] != 1 && matrix[i - 1][j - 2] != 1 && matrix[i - 2][j - 1] != 1)
					dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1];
			}
		}
		System.out.println(dp[0][N][N] + dp[1][N][N] + dp[2][N][N]);
	}

}