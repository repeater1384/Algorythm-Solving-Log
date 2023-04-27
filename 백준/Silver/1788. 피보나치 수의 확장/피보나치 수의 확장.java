import java.util.Scanner;

public class Main {
	static int MOD = 1_000_000_000;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		int a = 0, b = 1;
		for (int i = 0; i < Math.abs(n); i++) {
			int next = (a + b) % MOD;
			a = b;
			b = next;
		}

		System.out.println(n < 0 && n % 2 == 0 ? -1 : n == 0 ? 0 : 1);
		System.out.println(a);

		sc.close();
	}
}