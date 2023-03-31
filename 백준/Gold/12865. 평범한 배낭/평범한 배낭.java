import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] weight = new int[N + 1];
		int[] value = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			weight[i] = sc.nextInt();
			value[i] = sc.nextInt();
		}
		int[][] dp = new int[N + 1][K + 1];
		for (int i = 1; i <= N; i++) {
			for (int k = 1; k <= K; k++) {
				if (weight[i] <= k) {
					dp[i][k] = Math.max(dp[i - 1][k], dp[i - 1][k - weight[i]] + value[i]);
				}else {
					dp[i][k] = dp[i-1][k];
				}
			}
		}
		System.out.println(dp[N][K]);
		sc.close();
	}
}