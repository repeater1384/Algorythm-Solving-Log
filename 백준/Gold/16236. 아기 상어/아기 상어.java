import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

class Fish implements Comparable<Fish> {
	int x, y, distance;

	public Fish(int x, int y, int distance) {
		super();
		this.x = x;
		this.y = y;
		this.distance = distance;
	}

	@Override
	public int compareTo(Fish o) {
		if (this.distance == o.distance && this.y == o.y)
			return this.x - o.x;
		if (this.distance == o.distance)
			return this.y - o.y;
		return this.distance - o.distance;
	}

	@Override
	public String toString() {
		return "Fish [x=" + x + ", y=" + y + ", distance=" + distance + "]";
	}

}

public class Main {
	static int N;
	static int[][] arr;
	static int sharkX, sharkY, sharkSize = 2;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		arr = new int[N][N];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++) {
				arr[i][j] = sc.nextInt();
				if (arr[i][j] == 9) {
					sharkX = j;
					sharkY = i;
					arr[i][j] = 0;
				}
			}

		int answer = 0;
		int needEatFish = sharkSize;

		while (true) {
			Fish fish = findNearFish();
			if (fish == null)
				break;

			sharkX = fish.x;
			sharkY = fish.y;
			answer += fish.distance;

			arr[fish.y][fish.x] = 0;
			needEatFish--;
			if (needEatFish == 0) {
				sharkSize++;
				needEatFish = sharkSize;
			}

		}
		System.out.println(answer);
		sc.close();
	}

	static Fish findNearFish() {
		int[] dx = { 1, 0, -1, 0 };
		int[] dy = { 0, 1, 0, -1 };
		boolean[][] visited = new boolean[N][N];

		Queue<int[]> queue = new LinkedList<>();
		List<Fish> canEatFish = new ArrayList<>();

		queue.add(new int[] { sharkX, sharkY, 0 });
		visited[sharkY][sharkX] = true;

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int cx = cur[0];
			int cy = cur[1];
			int dis = cur[2];
			if (0 < arr[cy][cx] && arr[cy][cx] < sharkSize) {
				canEatFish.add(new Fish(cx, cy, dis));
			}
			for (int i = 0; i < 4; i++) {
				int nx = cx + dx[i];
				int ny = cy + dy[i];
				if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[ny][nx] && arr[ny][nx] <= sharkSize) {
					queue.add(new int[] { nx, ny, dis + 1 });
					visited[ny][nx] = true;
				}
			}
		}
		Collections.sort(canEatFish);
		return canEatFish.size() == 0 ? null : canEatFish.get(0);
	}
}