import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int weight[][] = new int[N + 2][M];
		int dp[][] = new int[N + 2][M];

		for (int i = 1; i <= N; i++) {
			String temp = sc.next();
			for (int j = 0; j < M; j++) {
				weight[i][j] = temp.charAt(j) - '0';
			}
		}

		int answer = 0;
		for (int i = 1; i <= N; i++) {
			for (int j = 0; j < M; j++) {
				if(j>0) {
					dp[i][j] = Math.max(dp[i - 1][j - 1], Math.max(dp[i][j - 1], dp[i + 1][j - 1])) + weight[i][j];
					answer = Math.max(answer, dp[i][j]);
				}else {
					dp[i][j] = weight[i][j];
				}
			}
		}
		
		System.out.println(answer);

	}
}
