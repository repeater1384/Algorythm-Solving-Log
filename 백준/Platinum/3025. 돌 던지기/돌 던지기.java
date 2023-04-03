import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		Stack<int[]>[] dp = new Stack[C];
		for (int col = 0; col < C; col++) {
			dp[col] = new Stack<int[]>();
		}

		char[][] matrix = new char[R + 1][C];
		for (int i = 0; i < R; i++)
			matrix[i] = br.readLine().toCharArray();
		for (int col = 0; col < C; col++)
			matrix[R][col] = 'X';
//		

		int N = Integer.parseInt(br.readLine());
		while (N-- > 0) {
			int COL = Integer.parseInt(br.readLine()) - 1;
			int col = -1;
			int row = -1;
			int[] last = null;
			while (!dp[COL].isEmpty()) {
				last = dp[COL].pop();
				if (matrix[last[0]][last[1]] == '.') {
					break;
				}
			}
			if (last == null) {
				row = 0;
				col = COL;
			} else {
				row = last[0];
				col = last[1];
			}

			for (; row < R; row++) {
				dp[COL].add(new int[] { row, col });

				if (matrix[row + 1][col] == '.') {
					continue;
				}
				if (matrix[row + 1][col] == 'X') {
					matrix[row][col] = 'O';
					break;
				}

				if (matrix[row + 1][col] == 'O') {
					if (col - 1 >= 0 && matrix[row][col - 1] == '.' && matrix[row + 1][col - 1] == '.') {
						col--;
						continue;
					}
					if (col + 1 < C && matrix[row][col + 1] == '.' && matrix[row + 1][col + 1] == '.') {
						col++;
						continue;
					}
					matrix[row][col] = 'O';
					break;

				}
			}
//			System.out.println("----------------------");
//			for (int c = 0; c < C; c++) {
//				System.out.print(c + " ");
//				for (int[] a : dp[c]) {
//					System.out.print(Arrays.toString(a));
//				}
//				System.out.println();
//			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < R; i++) {
			sb.append(matrix[i]).append('\n');
		}
		System.out.println(sb.toString());
		br.close();
	}
}
