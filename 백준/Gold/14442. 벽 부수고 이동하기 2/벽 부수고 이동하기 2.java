import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int K = sc.nextInt();
		int[][] matrix = new int[N][M];
		// minDistance[i][j][k] -> (i,j)까지 k번 벽 부수고 도달할 수 있는 최솟값
		int[][][] minDistance = new int[N][M][K+1];
		for (int i = 0; i < N; i++) {
			char[] temp = sc.next().toCharArray();
			for (int j = 0; j < M; j++) {
				matrix[i][j] = temp[j] - '0';
			}
		}

		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] { 0, 0, 0 });
		minDistance[0][0][0] = 1;

		int[] dx = { 1, 0, -1, 0 };
		int[] dy = { 0, 1, 0, -1 };

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int cx = cur[0];
			int cy = cur[1];
			int crash = cur[2];
			
			if(cx == M-1 && cy == N-1) {
				System.out.println(minDistance[cy][cx][crash]);
				System.exit(0);
			}
			
			for (int i = 0; i < 4; i++) {
				int nx = cx + dx[i];
				int ny = cy + dy[i];
				if (nx < 0 || M <= nx || ny < 0 || N <= ny)
					continue;
				if (matrix[ny][nx] == 1 && crash < K && minDistance[ny][nx][crash+1] == 0) {
					queue.add(new int[] { nx, ny, crash + 1 });
					minDistance[ny][nx][crash + 1] = minDistance[cy][cx][crash] + 1;
				}
				if (matrix[ny][nx] == 0 && minDistance[ny][nx][crash] == 0) {
					queue.add(new int[] { nx,ny, crash });
					minDistance[ny][nx][crash] = minDistance[cy][cx][crash] + 1;
				}
			}
		}
		
		System.out.println(-1);
	}
}