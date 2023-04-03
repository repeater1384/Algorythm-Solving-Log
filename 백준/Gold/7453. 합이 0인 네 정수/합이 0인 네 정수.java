import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int[][] ABCD = new int[N][4];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 4; j++) {
				ABCD[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int[] AB = new int[N * N];
		int[] CD = new int[N * N];
		int idx = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				AB[idx] = ABCD[i][0] + ABCD[j][1];
				CD[idx++] = ABCD[i][2] + ABCD[j][3];
			}
		}

		Arrays.sort(AB);
		Arrays.sort(CD);

		long answer = 0;

		// i는 AB, j는 CD
		int i = 0;
		int j = N * N - 1;
		while (i < N * N && j >= 0) {
			int sumAB = AB[i];
			int sumCD = CD[j];
			int sum = sumAB + sumCD;
			long ABcnt = 0;
			long CDcnt = 0;

			if (sum == 0) {
				while (i < N * N && sumAB == AB[i]) {
					i++;
					ABcnt++;
				}
				while (j >= 0 && sumCD == CD[j]) {
					j--;
					CDcnt++;
				}
				answer += ABcnt * CDcnt;
			} else if (sum > 0) {
				j--;
			} else {
				i++;
			}
		}
		System.out.println(answer);
	}
}