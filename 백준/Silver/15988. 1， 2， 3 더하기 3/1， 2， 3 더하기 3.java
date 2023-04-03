import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int MOD = 1_000_000_009;
		long[] dp = new long[1000001];
		dp[1] = 1;
		dp[2] = 2;
		dp[3] = 4;
		for (int i = 4; i <= 1000000; i++)
			dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD;

		int T = sc.nextInt();
		while (T-- > 0) {
			int N = sc.nextInt();
			System.out.println(dp[N]);
		}
		sc.close();
	}
}