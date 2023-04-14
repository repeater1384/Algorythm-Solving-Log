import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[][] matrix = new int[N][M];

		int answer = 0;

		for (int i = 0; i < N; i++) {
			String temp = sc.next();
			for (int j = 0; j < M; j++) {
				matrix[i][j] = temp.charAt(j) - '0';
			}
		}

		for (int size = 1; size <= Math.min(N, M); size++) {
			for (int i = 0; i <= N - size; i++) {
				for (int j = 0; j <= M - size; j++) {
					int temp = matrix[i][j];
					if (temp == matrix[i + size - 1][j] && temp == matrix[i + size - 1][j + size - 1]
							&& temp == matrix[i][j + size - 1])
						answer = size*size;
				}
			}
		}
		System.out.println(answer);

	}
}