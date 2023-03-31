import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		while (T-- > 0) {
			int N = Integer.parseInt(br.readLine());
			int[][] ranks = new int[N][2];
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				ranks[i] = new int[] { a, b };
			}
			
			Arrays.sort(ranks, (a, b) -> (a[0] - b[0]));
			
			int answer = 1;
			int needRank = ranks[0][1];
			for (int i = 1; i < N; i++) {
				if (needRank > ranks[i][1]) {
					needRank = ranks[i][1];
					answer++;
				}
			}
			System.out.println(answer);
		}
	}

}