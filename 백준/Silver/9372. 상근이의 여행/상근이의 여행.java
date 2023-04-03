import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int i = 0 ; i<T;i++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			for (int j = 0; j < M; j++) {
				sc.nextInt();
				sc.nextInt();
			}
			
			System.out.println(N - 1);
		}
	}
}