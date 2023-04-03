import java.util.Scanner;

class Shark {
	int speed, dir, size;

	public Shark(int speed, int dir, int size) {
		super();
		this.speed = speed;
		this.dir = dir;
		this.size = size;
	}

	public Shark eat(Shark other) {
		if (this.size > other.size)
			return this;
		return other;
	}

	@Override
	public String toString() {
		return "Shark [speed=" + speed + ", dir=" + dir + ", size=" + size + "]";
	}
}

public class Main {
	static int N;
	static int M;
	static Shark[][] matrix;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		int K = sc.nextInt();
		matrix = new Shark[N][M];

		while (K-- > 0) {
			int r = sc.nextInt() - 1;
			int c = sc.nextInt() - 1;
			int s = sc.nextInt();
			int d = sc.nextInt() - 1;
			int z = sc.nextInt();
			matrix[r][c] = new Shark(s, d, z);
		}

		int[] dc = { 0, 0, 1, -1 };
		int[] dr = { -1, 1, 0, 0 };

		int answer = 0;
		for (int col = 0; col < M; col++) {
			for (int row = 0; row < N; row++) {
				if (matrix[row][col] == null)
					continue;
				answer += matrix[row][col].size;
				matrix[row][col] = null;
				break;
			}

			Shark[][] temp = new Shark[N][M];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					if (matrix[i][j] == null)
						continue;
					int speed = matrix[i][j].speed;
					int dir = matrix[i][j].dir;
					if (dir == 0 || dir == 1)
						speed %= (2 * N - 2);
					else
						speed %= (2 * M - 2);
					int r = i;
					int c = j;
					while (speed-- > 0) {
						r += dr[dir];
						c += dc[dir];
						if (r < 0 || N <= r || c < 0 || M <= c) {
							if (dir == 0)
								dir = 1;
							else if (dir == 1)
								dir = 0;
							else if (dir == 2)
								dir = 3;
							else if (dir == 3)
								dir = 2;
							r += dr[dir] * 2;
							c += dc[dir] * 2;
						}
						matrix[i][j].dir = dir;
					}
					if (temp[r][c] == null) {
						temp[r][c] = matrix[i][j];
					} else {
						temp[r][c] = matrix[i][j].eat(temp[r][c]);
					}

				}
			}
			matrix = temp;
		}
		System.out.println(answer);
		sc.close();
	}
}