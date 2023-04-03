import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int N;
	static int M;
	static char[][] arr;
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, 1, 0, -1 };

	static int ex, ey, sx, sy;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		arr = new char[N][M];
		for (int i = 0; i < N; i++)
			arr[i] = sc.next().toCharArray();

		Queue<int[]> waterQueue = new LinkedList<>();
		Queue<int[]> mainQueue = new LinkedList<>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 'D') {
					ey = i;
					ex = j;
				}
				if (arr[i][j] == 'S') {
					sy = i;
					sx = j;
					mainQueue.add(new int[] { j, i });
					arr[i][j] = '.';
				}
				if (arr[i][j] == '*') {
					waterQueue.add(new int[] { j, i });
				}
			}
		}

		int curTime = 0;

		while (true) {
			Queue<int[]> next = new LinkedList<>();
			waterQueue = waterFlood(waterQueue);
			if (mainQueue.isEmpty())
				break;
//			printArr();
//			for (int[] is : mainQueue) {
//				System.out.println(Arrays.toString(is));
//			}
			while (!mainQueue.isEmpty()) {
				int[] cur = mainQueue.poll();
				int cx = cur[0];
				int cy = cur[1];
				if (cx == ex && cy == ey) {
					System.out.println(curTime);
					System.exit(0);
				}

				for (int i = 0; i < 4; i++) {
					int nx = cx + dx[i];
					int ny = cy + dy[i];
					if (0 <= nx && nx < M && 0 <= ny && ny < N && (arr[ny][nx] == '.' || arr[ny][nx] == 'D')) {
						arr[ny][nx] = 'S';
						next.add(new int[] { nx, ny });
					}
				}
			}
			curTime++;
			mainQueue = next;
		}

		System.out.println("KAKTUS");
		sc.close();
	}

	static Queue<int[]> waterFlood(Queue<int[]> waterQueue) {
		Queue<int[]> next = new LinkedList<>();
		while (!waterQueue.isEmpty()) {
			int[] cur = waterQueue.poll();
			int cx = cur[0];
			int cy = cur[1];
			for (int i = 0; i < 4; i++) {
				int nx = cx + dx[i];
				int ny = cy + dy[i];
				if (0 <= nx && nx < M && 0 <= ny && ny < N && (arr[ny][nx] == '.' || arr[ny][nx] == 'S')) {
					arr[ny][nx] = '*';
					next.add(new int[] { nx, ny });
				}
			}
		}
		return next;
	}

	static void printArr() {
		for (char[] cs : arr) {
			System.out.println(cs);
		}
		System.out.println();
	}
}
