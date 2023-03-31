import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while (T-- > 0) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			double answer = 1;
			for (int x = b - a + 1,y=1; x <= b; x++,y++) {
				answer *= x;
				answer /= y;
			}
			System.out.println((int)answer);
		}
		sc.close();
	}
}