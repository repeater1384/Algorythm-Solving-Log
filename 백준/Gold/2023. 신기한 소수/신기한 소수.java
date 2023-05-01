import java.util.Scanner;

public class Main {

	static int N;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		dfs("", 0);
		System.out.println(sb.toString());
		sc.close();
	}

	static void dfs(String str_num, int depth) {
		if (depth == N) {
			sb.append(str_num).append('\n');
			return;
		}
		for (int i = 1; i <= 9; i++) {
			if (isPrime(Integer.parseInt(str_num + i))) {
				dfs(str_num + i, depth + 1);
			}
		}

	}

	static boolean isPrime(int num) {
		if (num == 1)
			return false;

		for (int i = 2; i < (int) Math.sqrt(num) + 1; i++) {
			if (num % i == 0)
				return false;
		}
		return true;
	}
}