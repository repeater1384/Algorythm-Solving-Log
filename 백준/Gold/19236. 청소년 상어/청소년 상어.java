import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class Fish {
	int num, dir;

	public Fish(int num, int dir) {
		super();
		this.num = num;
		this.dir = dir;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + dir;
		result = prime * result + num;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Fish other = (Fish) obj;
		if (dir != other.dir)
			return false;
		if (num != other.num)
			return false;
		return true;
	}

}

public class Main {
	static int N = 4;
	static Fish[][] matrix;
	static int[] dx = { 0, -1, -1, -1, 0, 1, 1, 1 };
	static int[] dy = { -1, -1, 0, 1, 1, 1, 0, -1 };
	static int sharkDir;
	static int sharkX, sharkY;
	static int answer = 0;
	static final Fish empty = new Fish(-1, -1);
	static final Fish shark = new Fish(-100, -100);

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		matrix = new Fish[N][N];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				matrix[i][j] = new Fish(sc.nextInt(), sc.nextInt() - 1);

		// init, shark is Null empty is (-1,-1)
		int firstNum = matrix[0][0].num;
		int firstDir = matrix[0][0].dir;
		matrix[0][0] = shark;

		dfs(firstNum, 0, 0, firstDir);
		System.out.println(answer);
		sc.close();
	}

	static void dfs(int eatSum, int sharkX, int sharkY, int sharkDir) {
		moveFish();
//		System.out.println("-------------------------------" + eatSum + " " + sharkY + " " + sharkX + " " + sharkDir);
//		printFish();
		List<int[]> canEatFishPos = new ArrayList<>();
		int d = 1;
		while (true) {
			int nx = sharkX + dx[sharkDir] * d;
			int ny = sharkY + dy[sharkDir] * d;
			if (nx < 0 || 4 <= nx || ny < 0 || 4 <= ny)
				break;
			else {
				d++;
				if (matrix[ny][nx].equals(empty))
					continue;
				canEatFishPos.add(new int[] { nx, ny });
			}
		}
//		for (int[] is : canEatFishPos) {
//			System.out.println(Arrays.toString(is));
//		}

		if (canEatFishPos.isEmpty()) {
			answer = Math.max(answer, eatSum);
			return;
		}

		Fish[][] temp = copy(matrix);
		for (int[] pos : canEatFishPos) {
			int tX = pos[0];
			int tY = pos[1];
			int eatNum = matrix[tY][tX].num;
			int eatDir = matrix[tY][tX].dir;
			matrix[sharkY][sharkX] = empty;
			matrix[tY][tX] = shark;
			dfs(eatSum + eatNum, tX, tY, eatDir);
			matrix = copy(temp);
		}

	}

	static Fish[][] copy(Fish[][] orig) {
		Fish[][] result = new Fish[4][4];
		for (int i = 0; i < 4; i++)
			result[i] = orig[i].clone();
		return result;
	}

	static void printFish() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (matrix[i][j] == null)
					System.out.print("  ");
				else
					System.out.print(matrix[i][j].num + " ");
			}
			System.out.println();

		}
	}

	static void printFish2() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (matrix[i][j] == null)
					System.out.print("  ");
				else
					System.out.print(matrix[i][j].dir + " ");
			}
			System.out.println();

		}
	}

	static void moveFish() {
		int targetNum = 1;
		while (targetNum <= 16) {
			boolean findFish = false;
//			printFish();
//			System.out.println("------------------" + targetNum);
			loop: for (int y = 0; y < N; y++) {
				for (int x = 0; x < N; x++) {
					if (matrix[y][x].num == targetNum) {
						findFish = true;
						int dir = matrix[y][x].dir - 1;
						int cnt = 8;
						while (cnt-- > 0) {
							dir = (dir + 1) % 8;
							int nx = x + dx[dir];
							int ny = y + dy[dir];
							if (nx < 0 || 4 <= nx || ny < 0 || 4 <= ny)
								continue;
							if (matrix[ny][nx].equals(shark))
								continue;
							Fish temp = new Fish(targetNum, dir);
							matrix[y][x] = matrix[ny][nx];
							matrix[ny][nx] = temp;
							break;
						}
						targetNum++;
						break loop;
					}
				}
			}
			if (!findFish)
				targetNum++;

		}
	}
}