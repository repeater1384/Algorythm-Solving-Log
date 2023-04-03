import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static int N, M;
	static char[][] matrix;
	static boolean[][][][] visited;

	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static int answer = 12345;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] st = sc.nextLine().split(" ");
		N = Integer.parseInt(st[0]);
		M = Integer.parseInt(st[1]);

		matrix = new char[N][M];
		visited = new boolean[M][N][M][N];

		int rx, ry, bx, by;
		rx = ry = bx = by = 0;
		for (int i = 0; i < N; i++) {
			String temp = sc.nextLine();
			for (int j = 0; j < M; j++) {
				matrix[i][j] = temp.charAt(j);
				if (matrix[i][j] == 'R') {
					rx = j;
					ry = i;
				}
				if (matrix[i][j] == 'B') {
					bx = j;
					by = i;
				}
			}
		}
		bfs(rx, ry, bx, by);
		System.out.println(answer!=12345 ? answer : -1);

	}

	static void bfs(int rx, int ry, int bx, int by) {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] { rx, ry, bx, by, 1 });
		visited[rx][ry][bx][by] = true;

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int count = cur[4];
			if (count > 10) {
				answer = -1;
				return;
			}

			for (int i = 0; i < 4; i++) {
				int new_rx = cur[0];
				int new_ry = cur[1];
				int new_bx = cur[2];
				int new_by = cur[3];
				int red_dis = 0;
				int blue_dis = 0;

				while (matrix[new_ry + dy[i]][new_rx + dx[i]] != '#') {
					new_rx += dx[i];
					new_ry += dy[i];
					red_dis++;
					if (matrix[new_ry][new_rx] == 'O')
						break;
				}

				while (matrix[new_by + dy[i]][new_bx + dx[i]] != '#') {
					new_bx += dx[i];
					new_by += dy[i];
					blue_dis++;
					if (matrix[new_by][new_bx] == 'O')
						break;
				}
				if (matrix[new_by][new_bx] == 'O')
					continue;
				if (matrix[new_ry][new_rx] == 'O') {
					answer = count;
					return;
				}

				if (new_rx == new_bx && new_ry == new_by) {
					if (red_dis > blue_dis) {
						new_rx -= dx[i];
						new_ry -= dy[i];
					} else {
						new_bx -= dx[i];
						new_by -= dy[i];
					}
				}

				if (!visited[new_rx][new_ry][new_bx][new_by]) {
					queue.add(new int[] { new_rx, new_ry, new_bx, new_by, count + 1 });
					visited[new_rx][new_ry][new_bx][new_by] = true;
				}
			}
		}
	}
}