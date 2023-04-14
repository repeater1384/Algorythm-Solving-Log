import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int input = 0;
		do {
			input = scanner.nextInt();
			if (input != 0)
				System.out.println(countPrime(input));
		} while (input != 0);
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

	static int countPrime(int n) {
		int count = 0;
		for (int i = n + 1; i <= 2 * n; i++) {
			if (checkPrime(i))
				count++;
		}
		return count;
	}
}
