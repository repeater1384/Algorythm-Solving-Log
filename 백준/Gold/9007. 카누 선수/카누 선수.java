import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		while (T-- > 0) {
			st = new StringTokenizer(br.readLine());
			int K = Integer.parseInt(st.nextToken());
			int N = Integer.parseInt(st.nextToken());

			int[][] all_class = new int[4][N];
			for (int i = 0; i < 4; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++)
					all_class[i][j] = Integer.parseInt(st.nextToken());

			}

			int idx = 0;
			int[] possible1 = new int[N * N];
			int[] possible2 = new int[N * N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {

					possible1[idx] = all_class[0][i] + all_class[1][j];
					possible2[idx++] = all_class[2][i] + all_class[3][j];
				}
			}

			Arrays.sort(possible1);
			Arrays.sort(possible2);

			int min_diff = Integer.MAX_VALUE;
			int answer = 0;

			for (int p1 : possible1) {
				int cur_diff = getDiff(possible2, K - p1);
				int abs = Math.abs(cur_diff);

				if (min_diff > abs) {
					answer = cur_diff;
					min_diff = abs;
				} else if (min_diff == abs && cur_diff > 0) {
					answer = cur_diff;
				}

			}
			sb.append(K - answer).append("\n");
		}
		System.out.println(sb.toString());
		br.close();

	}

	static int getDiff(int[] data, int target) {
		int result = 0;
		int min_diff = Integer.MAX_VALUE;

		int start = 0;
		int end = data.length - 1;
		while (start <= end) {
			int mid = (start + end) / 2;

			int diff = target - data[mid];
			int abs = Math.abs(diff);

			if (abs < min_diff) {
				result = diff;
				min_diff = abs;
			} else if (abs == min_diff && diff > 0) {
				result = diff;
			}

			if (diff > 0)
				start = mid + 1;
			else if (diff < 0)
				end = mid - 1;
			else
				return 0;
		}

		return result;
	}
}