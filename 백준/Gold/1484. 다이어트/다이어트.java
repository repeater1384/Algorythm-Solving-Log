import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int a = 1, b = 1;
		boolean find = false;
		while (true) {
			int cur = calc(a, b);
			if (cur > N && a - b == 1)
				break;
			if (cur == N) {
				System.out.println(a++);
				find = true;
			} else if (cur > N)
				b++;
			else
				a++;
		}
		if (!find)
			System.out.println(-1);
		sc.close();
	}

	static int calc(int a, int b) {
		return (int) ((long) a * a - (long) b * b);
	}
}