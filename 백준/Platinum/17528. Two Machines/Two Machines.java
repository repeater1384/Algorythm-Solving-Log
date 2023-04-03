import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int MAX_SIZE = 250 * 250 + 1; // 작업개수 250개, 걸리는 시간 250
		int N = Integer.parseInt(br.readLine());
		int[] A = new int[N];
		int[] B = new int[N];

		int a_sum = 0;
		for (int i = 0; i < N; i++) {

			StringTokenizer st = new StringTokenizer(br.readLine());
			A[i] = Integer.parseInt(st.nextToken());
			B[i] = Integer.parseInt(st.nextToken());
			a_sum += A[i];

		}

		int[] dp = new int[MAX_SIZE];
		Arrays.fill(dp, Integer.MAX_VALUE);
		dp[a_sum] = 0;
		for (int i = 0; i < N; i++)
			for (int t = 0; t < MAX_SIZE; t++)
				if (dp[t] != Integer.MAX_VALUE)
					dp[t - A[i]] = Math.min(dp[t - A[i]], dp[t] + B[i]);

		int answer = Integer.MAX_VALUE;
		for (int t = 0; t < MAX_SIZE; t++)
			answer = Math.min(answer, Math.max(t, dp[t]));

		System.out.println(answer);

	}

}