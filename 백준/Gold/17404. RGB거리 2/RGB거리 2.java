import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		final int MAX_VALUE = 1_000_001;
		int N = Integer.parseInt(st.nextToken());
		
		int[][] arr = new int[N + 1][3];

		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int answer = MAX_VALUE;
		for(int startColor = 0 ; startColor<3;startColor++) {
			int[][] dp = new int[N + 1][3];
			for (int i = 1; i <= N; i++) {
				Arrays.fill(dp[i], MAX_VALUE);
			dp[1][startColor] = arr[1][startColor];
			}
			
			for(int i = 2 ;i<=N;i++) {
				dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2])+arr[i][0];
				dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2])+arr[i][1];
				dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1])+arr[i][2];
			}
			
			for(int c = 0 ; c<3;c++) {
				if(c==startColor)continue;
				answer = Math.min(answer,  dp[N][c]);
			}
				
		}
//		for (int j = 0; j < 3; j++)
//			dp[0][j] = arr[N][j];
//
//		for (int i = 1; i <= N; i++) {
//			for (int j = 0; j < 3; j++) {
//				for (int k = 0; k < 3; k++) {
//					if (k == j)
//						continue;
//					dp[i][j] = Math.min(dp[i][j], dp[i - 1][k] + arr[i][j]);
//				}
//			}
//		}
		
		System.out.println(answer);
	}

}