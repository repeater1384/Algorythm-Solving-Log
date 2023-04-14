import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] dx = { 0, 1, 0, -1 };
		int[] dy = { -1, 0, 1, 0 };
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[][] arr = new int[N][M];

		int y = sc.nextInt();
		int x = sc.nextInt();
		int dir = sc.nextInt();

		// 0 빈칸, 1 벽, 2 청소
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				arr[i][j] = sc.nextInt();

		int answer = 0;
		while (true) {
			if (arr[y][x] == 0) {
				arr[y][x] = 2;
				answer++;
			}

			int cnt = 4;
			while (cnt-- > 0) {
				dir = (dir + 3) % 4;
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				if (arr[ny][nx] == 0) {
					y = ny;
					x = nx;
					break;
				}
			}
			if (cnt >= 0)
				continue;

			int bx = x - dx[dir];
			int by = y - dy[dir];
			if (arr[by][bx] == 1)
				break;
			y = by;
			x = bx;
		}
		System.out.println(answer);
		sc.close();
	}
}