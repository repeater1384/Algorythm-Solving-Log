import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N;
	static int M;
	static char[][] matrix;
	static int answer = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		matrix = new char[N][M];
		for (int i = 0; i < N; i++) {
			char[] temp = sc.next().toCharArray();
			for (int j = 0; j < M; j++) {
				matrix[i][j] = temp[j];
			}
		}
		for (int i = 0; i < N; i++) {
			dfs(i, 0);
		}
		System.out.println(answer);
		sc.close();
	}

	private static boolean dfs(int i, int j) {
		// i번째 행에서 출발하는 dfs.
		matrix[i][j] = 'P';
		if (j == M - 1) {
			answer++;
			return true;
		}

		if (i - 1 >= 0 && matrix[i - 1][j + 1] == '.') {
			if (dfs(i - 1, j + 1))
				return true;
		}
		if (matrix[i][j + 1] == '.') {
			if (dfs(i, j + 1))
				return true;
		}
		if (i + 1 < N && matrix[i + 1][j + 1] == '.') {
			if (dfs(i + 1, j + 1))
				return true;

		}
		return false;
	}
}