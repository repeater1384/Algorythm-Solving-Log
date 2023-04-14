import java.util.Scanner;
import java.util.Stack;

public class Main {
	static char[][] matrix;
	static boolean[][] visited;
	static int sheep, wolf;
	static int N, M;
	static int[] deltaX = { 1, 0, -1, 0 };
	static int[] deltaY = { 0, 1, 0, -1 };

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();

		matrix = new char[N][M];
		visited = new boolean[N][M];
		sheep = wolf = 0;

		for (int i = 0; i < N; i++) {
			String temp = sc.next();
			for (int j = 0; j < M; j++) {
				matrix[i][j] = temp.charAt(j);
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if(!visited[i][j] && (matrix[i][j]=='v' || matrix[i][j] == 'k')) {
					dfs(j,i);
				}
			}
		}
		System.out.printf("%d %d",sheep,wolf);
		sc.close();
	}

	static void dfs(int sx, int sy) {
		int cur_sheep = 0;
		int cur_wolf = 0;
		Stack<int[]> stack = new Stack<>();
		stack.add(new int[] { sx, sy });
		visited[sy][sx] = true;
		
		while (stack.size() > 0) {
			int[] cur = stack.pop();
			int cx = cur[0];
			int cy = cur[1];
			
			if (matrix[cy][cx] == 'v')
				cur_wolf++;
			if (matrix[cy][cx] == 'k')
				cur_sheep++;

			for (int i = 0; i < 4; i++) {
				int nx = cx + deltaX[i];
				int ny = cy + deltaY[i];
				if (nx < 0 || M <= nx || ny < 0 || N <= ny)
					continue;
				if (visited[ny][nx] || matrix[ny][nx] == '#')
					continue;
				stack.add(new int[] { nx, ny });
				visited[ny][nx] = true;
			}
		}
//		 System.out.println(cur_sheep+" "+cur_wolf+" ");
		if (cur_sheep > cur_wolf)
			sheep += cur_sheep;
		else
			wolf += cur_wolf;
	}

}
