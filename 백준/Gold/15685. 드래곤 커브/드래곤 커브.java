import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] matrix = new int[101][101];
		int[] dx = { 1, 0, -1, 0 };
		int[] dy = { 0, -1, 0, 1 };
		int N = sc.nextInt();
		while (N-- > 0) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			int d = sc.nextInt();
			int g = sc.nextInt();
			int[] dragon = new int[1 << g];
			dragon[0] = d;
			int idx = 1;
			for (int i = 0; i < g; i++) {
				int len = 1 << i;
				for (int j = 0; j < len; j++)
					dragon[idx++] = (dragon[len - j - 1] + 1) % 4;
			}
			matrix[y][x] = 1;
			for (int dir : dragon) {
				x += dx[dir];
				y += dy[dir];
				matrix[y][x] = 1;
			}
		}

		int answer = 0;
		for (int i = 0; i < 100; i++)
			for (int j = 0; j < 100; j++)
				if (matrix[i][j] == 1 && matrix[i + 1][j] == 1 && matrix[i][j + 1] == 1 && matrix[i + 1][j + 1] == 1)
					answer++;
		System.out.println(answer);
		sc.close();
	}
}