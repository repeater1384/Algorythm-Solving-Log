import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int M, N, K, answer;
	static int[][] arr, farm;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());

		Queue<int[]> queue = new LinkedList<>();

		arr = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 1) {
					queue.add(new int[] { i, j });
				}
			}

		}

		int[] di = { 1, 0, -1, 0 };
		int[] dj = { 0, 1, 0, -1 };
		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int ci = cur[0];
			int cj = cur[1];
			for (int k = 0; k < 4; k++) {
				int ni = ci + di[k];
				int nj = cj + dj[k];
				if (0 <= ni && ni < N && 0 <= nj && nj < M && arr[ni][nj] == 0) {
					arr[ni][nj] = arr[ci][cj] + 1;
					queue.add(new int[] { ni, nj });
				}
			}
		}

		answer = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 0) {
					System.out.println(-1);
					System.exit(0);
				}
				answer = Math.max(answer, arr[i][j]);
			}

		}
		System.out.println(answer-1);
	}

}