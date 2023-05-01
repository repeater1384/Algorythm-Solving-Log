import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[][] matrix = new int[N][M];
		List<int[]> points = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				matrix[i][j] = sc.nextInt();
				if (matrix[i][j] == 1)
					points.add(new int[] { i, j });
			}
		}
		sc.close();

		int answer = Integer.MIN_VALUE;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (matrix[i][j] == 1)
					continue;
				int min_dis = Integer.MAX_VALUE;
				for (int[] point : points) {
					int y = point[0];
					int x = point[1];
					min_dis = Math.min(get_dis(i, j, y, x), min_dis);
				}
				answer = Math.max(min_dis, answer);
			}
		}
		System.out.println(answer);
	}

	static int get_dis(int i, int j, int y, int x) {
		int yDif = Math.abs(i - y);
		int xDif = Math.abs(j - x);
		return Math.max(yDif, xDif);
	}
}