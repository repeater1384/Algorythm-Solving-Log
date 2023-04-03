import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] sum = new int[N + 1];
		for (int i = 1; i <= N; i++)
			sum[i] = sum[i - 1] + sc.nextInt();

		while (M-- > 0) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			System.out.println(sum[b] - sum[a - 1]);
		}
		sc.close();
	}
}
