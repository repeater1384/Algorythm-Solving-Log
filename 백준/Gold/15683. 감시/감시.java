import java.util.Scanner;

class CCTV {
	int x, y, type;

	public CCTV(int x, int y, int type) {
		super();
		this.x = x;
		this.y = y;
		this.type = type;
	}

}

public class Main {
	static int N;
	static int M;
	static int[][] arr;
	static CCTV[] cctv;
	static int cctv_size;
	static int answer;
	static int[] cctv_dir;
	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		arr = new int[N][M];
		cctv = new CCTV[8];
		cctv_size = 0;
		cctv_dir = new int[] { 4, 2, 4, 4, 1 };

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				arr[i][j] = sc.nextInt();
				if (arr[i][j] != 0 && arr[i][j] != 6)
					cctv[cctv_size++] = new CCTV(j, i, arr[i][j] - 1);
			}
		}
		answer = Integer.MAX_VALUE;
		dfs(0);
		System.out.println(answer);

		sc.close();
	}

	static void dfs(int cctv_idx) {
		if (cctv_idx == cctv_size) {
			int cnt = 0;
			for (int i = 0; i < N; i++)
				for (int j = 0; j < M; j++)
					if (arr[i][j] == 0)
						cnt++;
			answer = Math.min(answer, cnt);
			return;
		}

		int[][] arr_copy = copy(arr);

		int cur_type = cctv[cctv_idx].type;
		int sx = cctv[cctv_idx].x;
		int sy = cctv[cctv_idx].y;

		for (int dir = 0; dir < cctv_dir[cur_type]; dir++) {
			// 1번 CCTV, 우/하/좌/상
			if (cur_type == 0) {
				move(sx,sy,dir);
			}
			// 2번 CCTV, 좌우 / 상하
			if (cur_type == 1) {
				move(sx,sy,dir);
				move(sx,sy,dir+2);
			}
			// 3번 CCTV, 상우 / 우하 / 하좌 / 좌상
			if (cur_type == 2) {
				move(sx,sy,dir);
				move(sx,sy,dir+1);
			}

			// 4번 CCTV, 상우하/ 우하좌 / 하좌상 / 좌상우
			if (cur_type == 3) {
				move(sx,sy,dir);
				move(sx,sy,dir+1);
				move(sx,sy,dir+2);
			}
			// 5번 CCTV, 상하좌우
			if (cur_type == 4) {
				move(sx,sy,dir);
				move(sx,sy,dir+1);
				move(sx,sy,dir+2);
				move(sx,sy,dir+3);
			}

			dfs(cctv_idx + 1);
			arr = copy(arr_copy);
		}
	}

	static int[][] copy(int[][] orig) {
		int[][] result = new int[orig.length][];
		for (int i = 0; i < orig.length; i++)
			result[i] = orig[i].clone();
		return result;
	}
	
	static void move(int x, int y, int dir) {
		dir %= 4;
		if(dir==0)right(x,y);
		if(dir==1)down(x,y);
		if(dir==2)left(x,y);
		if(dir==3)up(x,y);
	}
	static void down(int x, int y) {
		while (y + 1 < N) {
			y++;
			if (arr[y][x] == 6)
				break;
			if (arr[y][x] == 0)
				arr[y][x] = 9;
		}
	}

	static void up(int x, int y) {
		while (0 <= y - 1) {
			y--;
			if (arr[y][x] == 6)
				break;
			if (arr[y][x] == 0)
				arr[y][x] = 9;
		}
	}

	static void left(int x, int y) {
		while (0 <= x - 1) {
			x--;
			if (arr[y][x] == 6)
				break;
			if (arr[y][x] == 0)
				arr[y][x] = 9;
		}
	}

	static void right(int x, int y) {
		while (x + 1 < M) {
			x++;
			if (arr[y][x] == 6)
				break;
			if (arr[y][x] == 0)
				arr[y][x] = 9;
		}
	}
}