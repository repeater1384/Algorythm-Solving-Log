import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();
		long answer = 0;
		for (int i = 1; i < N; i++) {
			answer += N * i + i;
		}
		System.out.println(answer);
		sc.close();
	}
}