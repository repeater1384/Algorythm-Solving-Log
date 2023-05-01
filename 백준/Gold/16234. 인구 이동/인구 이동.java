import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int N, L, R;
	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { -1, 0, 1, 0 };
	static int[][] arr;
	static boolean[][] visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		L = sc.nextInt();
		R = sc.nextInt();
		arr = new int[N][N];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				arr[i][j] = sc.nextInt();

		int answer = 0;
		while (true) {
//			for (int[] i : arr) {
//				System.out.println(Arrays.toString(i));
//			}
			visited = new boolean[N][N];
			boolean changed = false;
			for(int i = 0 ;i<N;i++) {
				for(int j = 0 ;j<N;j++) {
					if(!visited[i][j])
						changed |= bfs(j,i);
				}
			}
			
			if(!changed)break;
			answer++;
		}
		System.out.println(answer);

		sc.close();
	}

	static boolean bfs(int sx, int sy) {
		// 두개 이상 바꾸면 true
		Queue<int[]> queue = new LinkedList<>();

		queue.add(new int[] { sx, sy });
		visited[sy][sx] = true;
		List<int[]> allPos = new ArrayList<>();

		int unionSum = 0;
		int unionSize = 0;
		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int cx = cur[0];
			int cy = cur[1];
//			System.out.println(cx+" "+cy);
			unionSum += arr[cy][cx];
			unionSize++;
			allPos.add(new int[] { cx, cy });

			for (int i = 0; i < 4; i++) {
				int nx = cx + dx[i];
				int ny = cy + dy[i];
				if (nx < 0 || N <= nx || ny < 0 || N <= ny || visited[ny][nx])
					continue;
				if (check(arr[cy][cx], arr[ny][nx])) {
					queue.add(new int[] { nx, ny });
					visited[ny][nx] = true;
				}
			}
		}

		int unionAvg = unionSum / unionSize;
		for (int[] cur : allPos) {
			int x = cur[0];
			int y = cur[1];
			arr[y][x] = unionAvg;
		}
		return allPos.size() >= 2;

	}

	static boolean check(int a, int b) {
		int diff = Math.abs(a - b);
		return L <= diff && diff <= R;
	}
}