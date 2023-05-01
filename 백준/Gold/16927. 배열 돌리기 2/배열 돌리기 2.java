import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());

		int outlineSize = Math.min(N, M) / 2;
		List<LinkedList<Integer>> outline = new ArrayList<LinkedList<Integer>>();

		int[][] arr = new int[N][M];
		int rowFlag1 = 0, rowFlag2 = N - 1;
		int colFlag1 = 0, colFlag2 = M - 1;

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++)
				arr[i][j] = Integer.parseInt(st.nextToken());
		}

		int[] dx = { 1, 0, -1, 0 };
		int[] dy = { 0, 1, 0, -1 };
		int sx = 0, sy = 0;
		for (int i = 0; i < outlineSize; i++) {
			outline.add(new LinkedList<Integer>());
			outline.get(i).add(arr[sy][sx]);
			arr[sy][sx] = 0;

			int cx = sx;
			int cy = sy;
			for (int di = 0; di < 4; di++) {
				while (true) {
					int nx = cx + dx[di];
					int ny = cy + dy[di];
					if (0 <= nx && nx < M && 0 <= ny && ny < N && arr[ny][nx] != 0) {
						outline.get(i).add(arr[ny][nx]);
						arr[ny][nx] = 0;
						cx = nx;
						cy = ny;
					} else
						break;

				}

			}
			sx++;
			sy++;

		}
		for (int i = 0; i < outlineSize; i++) {
			int curR = R % outline.get(i).size();
			LinkedList<Integer> cur = outline.get(i);
			while (curR-- > 0)
				cur.add(cur.poll());
		}

		sx = 0;
		sy = 0;
		for (int i = 0; i < outlineSize; i++) {
			LinkedList<Integer> cur = outline.get(i);
			int cur_idx = 0;

			arr[sy][sx] = cur.get(cur_idx++);

			int cx = sx;
			int cy = sy;
			for (int di = 0; di < 4; di++) {
				while (true) {
					int nx = cx + dx[di];
					int ny = cy + dy[di];
					if (0 <= nx && nx < M && 0 <= ny && ny < N && arr[ny][nx] == 0) {
						arr[ny][nx] = cur.get(cur_idx++);
						cx = nx;
						cy = ny;
					} else
						break;
				}
			}
			sx++;
			sy++;

		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++)
				sb.append(arr[i][j]).append(' ');
			sb.append('\n');
		}
		System.out.println(sb.toString());
		br.close();
	}

}