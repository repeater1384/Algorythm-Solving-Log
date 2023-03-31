import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while (T-- > 0) {
			int N = sc.nextInt();
			int[] coin = new int[N + 1];
			for (int i = 1; i <= N; i++) {
				coin[i] = sc.nextInt();
			}
			int K = sc.nextInt();
			int[][] dp = new int[N + 1][K + 1];
			for (int i = 1; i <= N; i++)
				dp[i][0] = 1;
			for (int i = 1; i <= N; i++) {
				for (int k = 1; k <= K; k++) {
					if (coin[i] <= k)
						dp[i][k] = dp[i - 1][k] + dp[i][k - coin[i]];
					else
						dp[i][k] = dp[i - 1][k];
				}
			}

			System.out.println(dp[N][K]);
		}
		sc.close();
	}

}