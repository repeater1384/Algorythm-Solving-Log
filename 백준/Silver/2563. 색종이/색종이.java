import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] matrix = new int[101][101];
		int answer = 0, T = sc.nextInt();
		while (T-- > 0) {
			int a = sc.nextInt(), b = sc.nextInt();
			for (int i = a; i++ < a + 10;)
				for (int j = b; j++ < b + 10;)
					if (matrix[i][j] == 0)
						matrix[i][j] = ++answer;
		}
		System.out.println(answer);
		sc.close();
	}
}