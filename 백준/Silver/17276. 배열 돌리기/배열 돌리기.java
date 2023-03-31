import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[][] arr;
	static int N;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		while (T-- > 0) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			int D = Integer.parseInt(st.nextToken());
			int rotateCnt = D >= 0 ? D % 360 / 45 : (360 - Math.abs(D) % 360) / 45;

			arr = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++)
					arr[i][j] = Integer.parseInt(st.nextToken());
			}

			while (rotateCnt-- > 0)
				rotate45();

			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < N; i++) {
				sb.append(Arrays.toString(arr[i]).replace("[", "").replace("]", "").replace(",", "")).append('\n');
			}
			System.out.print(sb.toString());
		}
		br.close();
	}

	static void rotate45() {
		int[] line1 = new int[N];
		int[] line2 = new int[N];
		int[] line3 = new int[N];
		int[] line4 = new int[N];

		for (int i = 0; i < N; i++) {
			line1[i] = arr[i][i];
			line2[i] = arr[i][N / 2];
			line3[i] = arr[i][N - i - 1];
			line4[i] = arr[N / 2][N - i - 1];
		}
		for (int i = 0; i < N; i++) {
			arr[i][i] = line4[N - i - 1];
			arr[i][N / 2] = line1[i];
			arr[i][N - i - 1] = line2[i];
			arr[N / 2][N - i - 1] = line3[i];
		}
	}

}