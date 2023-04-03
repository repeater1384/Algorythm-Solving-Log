import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.lang.StringBuilder;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String S = br.readLine();

		int[][] prefixSum = new int[S.length()][26];
		prefixSum[0][S.charAt(0) - 'a']++;

		for (int i = 1; i < S.length(); i++) {
			for (int j = 0; j < 26; j++) {
				prefixSum[i][j] = prefixSum[i - 1][j];
			}
			prefixSum[i][S.charAt(i) - 'a']++;
		}

		StringBuilder sb = new StringBuilder();

		int query = Integer.parseInt(br.readLine());
		while (query-- > 0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int target = st.nextToken().charAt(0) - 'a';
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			if (start == 0) {
				sb.append(prefixSum[end][target]).append('\n');
			}else {
				sb.append(prefixSum[end][target] - prefixSum[start - 1][target]).append('\n');
			}
		}
		System.out.println(sb);
	}
}