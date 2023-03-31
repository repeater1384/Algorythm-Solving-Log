import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		// W->무게 V->만족도
		List<Integer> W = new ArrayList<>();
		List<Integer> V = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int w = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());

			int bit = 0;
			while (k > 0) {
				int cur = Math.min(1 << bit, k);
				W.add(w * cur);
				V.add(v * cur);
				bit++;
				k -= cur;
			}
		}
		int[][] dp = new int[W.size() + 1][M + 1];

		for (int i = 1; i <= W.size(); i++) {
			for (int j = 1; j <= M; j++) {
				if (j >= W.get(i - 1))
					dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - W.get(i - 1)] + V.get(i - 1));
				else
					dp[i][j] = dp[i - 1][j];
			}
		}
		System.out.println(dp[W.size()][M]);
	}

}