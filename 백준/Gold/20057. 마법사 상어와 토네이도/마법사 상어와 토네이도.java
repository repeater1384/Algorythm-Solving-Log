import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {

	static int N;
	static int[][] arr;
	static int answer = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		arr = new int[N][N];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				arr[i][j] = sc.nextInt();
		int cx = N / 2;
		int cy = N / 2;
		List<Integer> moveAmount = new ArrayList<>();
		for (int i = 1; i < N; i++) {
			moveAmount.add(i);
			moveAmount.add(i);
		}
		moveAmount.add(N - 1);
		int moveIdx = 0;
		int[] dx = { -1, 0, 1, 0 };
		int[] dy = { 0, 1, 0, -1 };
		for (int move : moveAmount) {
			while (move-- > 0) {
				int nx = cx + dx[moveIdx];
				int ny = cy + dy[moveIdx];
				moveDust(cx, cy, nx, ny);
				cx = nx;
				cy = ny;
			}
			moveIdx = (moveIdx + 1) % 4;
		}
		System.out.println(answer);
		sc.close();

	}

	static void moveDust(int ax, int ay, int bx, int by) {
		// a에서b로 토네이도가 불때, 움직임 구현.

		// dx,dy, 움직일 먼지 양, left기준.
		int[][] winds = { { 1, -1, 1 }, { 1, 1, 1 }, { 0, -1, 7 }, { 0, 1, 7 }, { 0, -2, 2 }, { 0, 2, 2 },
				{ -1, -1, 10 }, { -1, 1, 10 }, { -2, 0, 5 } };

		int curDust = arr[by][bx];
		int alpha = curDust;
		int x = bx - ax;
		int y = by - ay;
		if (x == -1 && y == 0) {
			for (int[] wind : winds) {
				int dx = wind[0];
				int dy = wind[1];
				int amount = curDust * wind[2] / 100;
				if (isInArea(bx + dx, by + dy)) {
					arr[by + dy][bx + dx] += amount;
				} else {
					answer += amount;
				}
				alpha -= amount;
			}
			arr[by][bx] = 0;
			if (isInArea(bx + x, by + y))
				arr[by + y][bx + x] += alpha;
			else
				answer += alpha;
		}
		if (x == 1 && y == 0) {
			for (int[] wind : winds) {
				int dx = -1 * wind[0];
				int dy = wind[1];
				int amount = curDust * wind[2] / 100;
				if (isInArea(bx + dx, by + dy)) {
					arr[by + dy][bx + dx] += amount;
				} else {
					answer += amount;
				}
				alpha -= amount;
			}
			arr[by][bx] = 0;
			if (isInArea(bx + x, by + y))
				arr[by + y][bx + x] += alpha;
			else
				answer += alpha;
		}
		if (x == 0 && y == -1) {
			for (int[] wind : winds) {
				int dx = -1 * wind[1];
				int dy = wind[0];
				int amount = curDust * wind[2] / 100;
				if (isInArea(bx + dx, by + dy)) {
					arr[by + dy][bx + dx] += amount;
				} else {
					answer += amount;
				}
				alpha -= amount;
			}
			arr[by][bx] = 0;
			if (isInArea(bx + x, by + y))
				arr[by + y][bx + x] += alpha;
			else
				answer += alpha;
		}

		if (x == 0 && y == 1) {
			for (int[] wind : winds) {
				int dx = -1 * wind[1];
				int dy = -1 * wind[0];
				int amount = curDust * wind[2] / 100;
				if (isInArea(bx + dx, by + dy)) {
					arr[by + dy][bx + dx] += amount;
				} else {
					answer += amount;
				}
				alpha -= amount;
			}
			arr[by][bx] = 0;
			if (isInArea(bx + x, by + y))
				arr[by + y][bx + x] += alpha;
			else
				answer += alpha;
		}
	}

	static boolean isInArea(int x, int y) {
		return 0 <= x && x < N && 0 <= y && y < N;
	}
}