import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int C = sc.nextInt();
		int D = sc.nextInt();
		int M = sc.nextInt();
		int[][] stocks = new int[C][D];
		for (int i = 0; i < C; i++)
			for (int j = 0; j < D; j++)
				stocks[i][j] = sc.nextInt();

		int[] dp;
		for (int day = 1; day < D; day++) {
			dp = new int[500001];
			for (int c = 0; c < C; c++) {
				for (int money = 0; money <= M; money++) {
					if (money >= stocks[c][day - 1]) {
						dp[money] = Math.max(dp[money],
								dp[money - stocks[c][day - 1]] + stocks[c][day] - stocks[c][day - 1]);
					}
				}
			}
			M += dp[M];
		}
		System.out.println(M);
		sc.close();
	}

}