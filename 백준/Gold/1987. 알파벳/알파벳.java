import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static int N, M, arr[][];
	static int answer = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		arr = new int[N][M];
		for (int i = 0; i < N; i++) {
			String temp = sc.next();
			for (int j = 0; j < M; j++)
				arr[i][j] = temp.charAt(j) - 'A';

		}
		dfs(1, new boolean[26], 0, 0);
		System.out.println(answer);
		sc.close();
	}

	static void dfs(int depth, boolean[] visited, int x, int y) {
		answer = Math.max(answer, depth);
		visited[arr[y][x]] = true;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (0 <= nx && nx < M && 0 <= ny && ny < N && !visited[arr[ny][nx]])
				dfs(depth + 1, visited, nx, ny);
		}
		visited[arr[y][x]] = false;
	}
}