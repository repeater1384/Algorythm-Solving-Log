import java.util.Scanner;

public class Main {
	static long[] count;
	static int weight;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = 1;
		int B = sc.nextInt();

		count = new long[10];
		weight = 1;

		while (A <= B) {
			while (B % 10 != 9 && A <= B) {
				calc(B);
				B--;
			}
			if (A > B)
				break;

			while (A % 10 != 0 && A <= B) {
				calc(A);
				A++;
			}

			A /= 10;
			B /= 10;

			for (int i = 0; i < 10; i++)
				count[i] += (B - A + 1) * weight;

			weight *= 10;
		}

		for (long digit : count) {
			System.out.print(digit + " ");
		}
		sc.close();
	}

	static void calc(int num) {
		while (num > 0) {
			count[num % 10] += weight;
			num /= 10;
		}
	}
}