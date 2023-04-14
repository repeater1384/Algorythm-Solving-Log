import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int N;
	static int[][] arr;
	static char[][] contour;
	static boolean[][] visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		arr = new int[N][N];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				arr[i][j] = sc.nextInt();

		int answer = Integer.MAX_VALUE;
		for (int r = 0; r <= N; r++) {
			for (int c = 1; c <= N; c++) {
				for (int d1 = 1; d1 <= N; d1++) {
					for (int d2 = 1; d2 <= N; d2++) {
						if (r + d1 + d2 < N && c - d1 >= 0 && c + d2 < N) {
							drawContour(r, c, d1, d2);
							int[] sum = new int[5];
							for (int i = 0; i < N; i++) {
								for (int j = 0; j < N; j++) {
									sum[contour[i][j] - 'A'] += arr[i][j];
								}
							}
							int min = Integer.MAX_VALUE;
							int max = Integer.MIN_VALUE;
							for (int k = 0; k < 5; k++) {
								min = Math.min(sum[k], min);
								max = Math.max(sum[k], max);
							}
							answer = Math.min(answer, max - min);
						}
					}
				}
			}
		}
		System.out.println(answer);
		sc.close();
	}

	static void drawContour(int r, int c, int d1, int d2) {
		contour = new char[N][N];
		for (int i = 0; i < N; i++)
			Arrays.fill(contour[i], '.');
		for (int i = 0; i <= d1; i++) {
			contour[r + i][c - i] = 'E';
			contour[r + d2 + i][c + d2 - i] = 'E';
		}
		for (int i = 0; i <= d2; i++) {
			contour[r + i][c + i] = 'E';
			contour[r + d1 + i][c - d1 + i] = 'E';
		}
		for (int i = 0; i < r; i++)
			contour[i][c] = 'A';
		for (int j = c + d2 + 1; j < N; j++)
			contour[r + d2][j] = 'B';
		for (int j = 0; j < c - d1; j++)
			contour[r + d1][j] = 'C';
		for (int i = r + d1 + d2 + 1; i < N; i++)
			contour[i][c - d1 + d2] = 'D';

		visited = new boolean[N][N];

//		for (char[] row : contour)
//			System.out.println(row);
//		System.out.println();

		fillArray('A', 0, 0);
		fillArray('B', N - 1, 0);
		fillArray('C', 0, N - 1);
		fillArray('D', N - 1, N - 1);
		fillArray('E', c, r);
//
//		for (char[] row : contour)
//			System.out.println(row);
//		System.out.println();
	}

	static void fillArray(char alpha, int sx, int sy) {
		int[] dx = { -1, 0, 1, 0 };
		int[] dy = { 0, 1, 0, -1 };

		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] { sx, sy });
		visited[sy][sx] = true;
		contour[sy][sx] = alpha;

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int cx = cur[0];
			int cy = cur[1];
			contour[cy][cx] = alpha;
			for (int i = 0; i < 4; i++) {
				int nx = cx + dx[i];
				int ny = cy + dy[i];
				if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[ny][nx]) {
					if ((alpha == 'E' && contour[ny][nx] == 'E') || contour[ny][nx] == '.') {
						queue.add(new int[] { nx, ny });
						visited[ny][nx] = true;
					}
				}
			}
		}
	}
}