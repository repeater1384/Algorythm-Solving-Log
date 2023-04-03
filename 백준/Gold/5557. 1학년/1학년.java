import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N;
	static int[] arr;
	static int target;
	static long[][] dp;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		arr = new int[N - 1];
		dp = new long[N - 1][21];
		for (int i = 0; i < N - 1; i++) {
			arr[i] = sc.nextInt();
			Arrays.fill(dp[i], -1);
		}
		target = sc.nextInt();

		dfs(0, 0);
		System.out.println(dp[0][0]);
//		for (long[] d : dp)
//			System.out.println(Arrays.toString(d));
		sc.close();
	}

	static long dfs(int depth, int result) {
		if (depth == N - 1)
			return result == target ? 1 : 0;

		if (dp[depth][result] != -1)
			return dp[depth][result];

		long cur = 0;
		if (checkBoundary(result + arr[depth]))
			cur += dfs(depth + 1, result + arr[depth]);
		if (depth != 0 && checkBoundary(result - arr[depth]))
			cur += dfs(depth + 1, result - arr[depth]);

		return dp[depth][result] = cur;

	}

	static boolean checkBoundary(int n) {
		return 0 <= n && n <= 20;
	}
}