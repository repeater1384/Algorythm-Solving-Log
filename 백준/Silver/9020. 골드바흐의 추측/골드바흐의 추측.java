import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int T = scanner.nextInt();
		int[] arr = new int[T];
		for (int i = 0; i < T; i++) {
			arr[i] = scanner.nextInt();
			goldBach(arr[i]);
		}

	}

	static boolean checkPrime(int n) {
		if (n == 2)
			return true;
		if (n <= 1)
			return false;
		for (int i = 2; i < Math.sqrt(n) + 1; i++)
			if (n % i == 0)
				return false;

		return true;
	}

	static void goldBach(int k) {
		int i, j;
		for (i = j = k / 2; i < k; i++, j--) {
			if (checkPrime(i) && checkPrime(j)) {
				System.out.printf("%d %d\n", j, i);
				break;
			}
		}
	}
}
