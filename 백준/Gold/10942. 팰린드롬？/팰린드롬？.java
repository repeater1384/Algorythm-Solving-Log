import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.lang.StringBuilder;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String[] str_num = br.readLine().split(" ");
		int[] num = new int[N];
		for (int i = 0; i < N; i++) {
			num[i] = Integer.parseInt(str_num[i]);
		}

		boolean[][] dp = new boolean[N][N];

		for (int i = 0; i < N; i++) {
			dp[i][i] = true;
		}
		for (int i = 0; i < N - 1; i++) {
			if (num[i] == num[i + 1]) {
				dp[i][i + 1] = true;
				dp[i + 1][i] = true;

			}
		}
		
		for(int i = 2 ; i<N;i++) {
			for(int j = 0 ; j<N-i;j++) {
				dp[j][j+i] = dp[j+1][j] =  (num[j]==num[j+i] && dp[j+1][j+i-1]);
			}
		}
		int M = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for(int i = 0 ;i<M;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken())-1;
			int e = Integer.parseInt(st.nextToken())-1;
			sb.append(dp[s][e] ? "1\n" : "0\n");
		}
		System.out.println(sb);

	}
}