import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[][] matrix = new int[N][M];
		int[][] dp = new int[N][M];
		for (int i = 0; i < N; i++) {
			String temp = sc.next();
			for (int j = 0; j < M; j++) {
				matrix[i][j] = temp.charAt(j) - '0';
				if (matrix[i][j] != 0 && (i == 0 || j == 0))
					dp[i][j] = 1;
			}
		}
		for (int i = 1; i < N; i++) {
			for (int j = 1; j < M; j++) {
				if (matrix[i][j] != 0)
					dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1])) + 1;
			}
		}
		int answer = 0;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				answer = Math.max(answer, dp[i][j] * dp[i][j]);
		System.out.println(answer);
		sc.close();
	}

}