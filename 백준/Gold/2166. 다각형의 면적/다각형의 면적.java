import java.util.Scanner;
import java.lang.Math;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[][] coords = new long[N + 1][2];
		for (int i = 0; i < N; i++) {
			long a = sc.nextLong();
			long b = sc.nextLong();
			coords[i][0] = a;
			coords[i][1] = b;
		}
		
		coords[N][0] = coords[0][0];
		coords[N][1] = coords[0][1];
		long plus = 0L, minus = 0;
		for (int i = 0; i < N; i++) {
			plus += coords[i][0] * coords[i + 1][1];
			minus += coords[i][1] * coords[i + 1][0];
		}
		String answer = String.format("%.1f",Math.abs(plus-minus)*0.5);
		System.out.println(answer);
	}

}
