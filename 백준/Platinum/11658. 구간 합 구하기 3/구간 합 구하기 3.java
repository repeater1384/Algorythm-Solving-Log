import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	static int[][] tree;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		tree = new int[N + 1][N + 1];
		int[][] arr = new int[N + 1][N + 1];

		for (int i = 1; i < N + 1; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j < N + 1; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				// 0으로 initialize되어있음. 들어오는 숫자가 바로 diff임.
				update(i, j, arr[i][j]);
			}
		}
//		for (int row[] : tree) {
//			for (int col : row) {
//				System.out.printf("%d ", col);
//			}
//			System.out.println();
//		}

		for (int i = 0; i < M; i++) {

			st = new StringTokenizer(br.readLine());
			int flag = Integer.parseInt(st.nextToken());

			if (flag == 0) {
				int y = Integer.parseInt(st.nextToken());
				int x = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				int diff = c - arr[y][x];
				arr[y][x] = c;
				update(y, x, diff);
			} else {
				int y1 = Integer.parseInt(st.nextToken());
				int x1 = Integer.parseInt(st.nextToken());
				int y2 = Integer.parseInt(st.nextToken());
				int x2 = Integer.parseInt(st.nextToken());
				long answer = sum(y2, x2) - sum(y2, x1 - 1) - sum(y1 - 1, x2) + sum(y1 - 1, x1 - 1);
				System.out.println(answer);

			}
		}

	}

	static long sum(int row, int col) {
		long answer = 0;
		int init_col = col;

		while (row > 0) {
			col = init_col;
			while (col > 0) {
				answer += tree[row][col];
				col -= (col & -col);
			}
			row -= (row & -row);
		}
		return answer;
	}

	static void update(int row, int col, int diff) {	
		int init_col = col;

		while (row < tree.length) {
			col = init_col;
			while (col < tree.length) {
				tree[row][col] += diff;
				col += (col & -col);
			}
			row += (row & -row);
		}
	}
}
