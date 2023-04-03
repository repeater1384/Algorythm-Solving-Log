import java.util.*;

public class Main {

	static int N, M, answer;
	static int[] dx = { 1, -1, 0, 0 }, dy = { 0, 0, 1, -1 };
	static int[][] matrix;
	static List<int[]> virus = new ArrayList<int[]>();

	static void wall(int cur, int cnt) {
		if (cnt == 3) {
			spread(matrix);
			return;
		}
		for (int idx = cur; idx < N * M; idx++) {
			int i = idx / M;
			int j = idx % M;
			if (matrix[i][j] == 0) {
				matrix[i][j] = 1;
				wall(idx + 1, cnt + 1);
				matrix[i][j] = 0;
			}
		}
	}

	static void spread(int[][] matrix) {
		Queue<int[]> queue = new LinkedList<int[]>(virus);
		boolean visited[][] = new boolean[N][M];
		for (int[] cur : queue) {
			int cy = cur[0];
			int cx = cur[1];
			visited[cy][cx] = true;
		}

		while (!queue.isEmpty()) {
			int[] virus = queue.poll();
			int cy = virus[0];
			int cx = virus[1];
			for (int i = 0; i < 4; i++) {
				int ny = cy + dy[i];
				int nx = cx + dx[i];
				if (ny < 0 || ny >= N || nx < 0 || nx >= M || visited[ny][nx] || matrix[ny][nx] == 1) {
					continue;
				}
				visited[ny][nx] = true;
				queue.add(new int[] { ny, nx });
			}
		}

		int safetyArea = 0;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				if (!visited[i][j] && matrix[i][j] != 1)
					safetyArea++;
		answer = Math.max(answer, safetyArea);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		matrix = new int[N][M];
		answer = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				matrix[i][j] = sc.nextInt();
				if (matrix[i][j] == 2)
					virus.add(new int[] { i, j });

			}
		}

		wall(0, 0);
		System.out.println(answer);
		sc.close();
	}
}