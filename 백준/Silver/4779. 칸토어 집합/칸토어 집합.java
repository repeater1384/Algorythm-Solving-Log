import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static char[] result;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			try {
				int N = sc.nextInt();
				result = new char[(int) Math.pow(3, N)];
				Arrays.fill(result, '-');
				dfs(N, 0);
				System.out.println(String.valueOf(result));
			} catch (Exception e) {
				break;
			}
		}
		sc.close();
	}

	static void dfs(int depth, int idx) {
		if (depth == 0)
			return;

		int temp = (int) Math.pow(3, depth - 1);
		for (int di = 0; di < temp; di++) 
			result[idx + temp + di] = ' ';
		
		dfs(depth - 1, idx);
		dfs(depth - 1, idx + temp * 2);
	}
}