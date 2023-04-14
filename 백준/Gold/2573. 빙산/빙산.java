import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int N;
	static int M;
	static int[][] matrix;
	static List<int[]> ice;
	static int[] dx = { 1, -1, 0, 0 };
	static int[] dy = { 0, 0, 1, -1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		matrix = new int[N][M];
		ice = new ArrayList<>();
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++) {
				matrix[i][j] = sc.nextInt();
				if (matrix[i][j] > 0)
					ice.add(new int[] { i, j });
			}

		int answer = 0;
		int year = 0;
		while (true) {
			if(ice.size() == 0)
				break;
			year++;
			
			// 빙산 녹이기
			int[][] nextMatrix = new int[N][M];
			List<int[]> nextIce = new ArrayList<>();

			for (int[] cur : ice) {
				int cy = cur[0];
				int cx = cur[1];

				int air = 0;
				for (int k = 0; k < 4; k++)
					if (matrix[cy + dy[k]][cx + dx[k]] == 0)
						air++;

				nextMatrix[cy][cx] = Math.max(0, matrix[cy][cx] - air);
				if (nextMatrix[cy][cx] > 0)
					nextIce.add(new int[] { cy, cx });
			}

			matrix = nextMatrix;
			ice = nextIce;

			// 분리된 빙산 개수 세기
			int cnt = bfs();
			if (cnt >= 2) {
				answer = year;
				break;
			}
		}
		
		System.out.println(answer);
		sc.close();
	}

	static int bfs() {
		boolean[][] visited = new boolean[N][M];
		int[][] temp = new int[N][M];
		int cnt = 0;

		for (int i = 0; i < N; i++)
			temp[i] = matrix[i].clone();
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (temp[i][j] > 0) {
					cnt++;
					Queue<int[]> queue = new LinkedList<>();
					queue.add(new int[] { i, j });
					visited[i][j] = true;
					while (!queue.isEmpty()) {
						int[] cur = queue.poll();
						int cy = cur[0];
						int cx = cur[1];
						temp[cy][cx] = 0;
						for (int k = 0; k < 4; k++) {
							int ny = cy + dy[k];
							int nx = cx + dx[k];
							if (temp[ny][nx] > 0 && !visited[ny][nx]) {
								queue.add(new int[] { ny, nx });
								visited[ny][nx] = true;
							}
						}
					}
				}
			}
		}
		return cnt;
	}
}