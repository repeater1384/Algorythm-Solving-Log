import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] arr = new int[N];
		for (int i = 0; i < N; i++)
			arr[i] = sc.nextInt();
		Arrays.sort(arr);
		Combination cm = new Combination(arr, M);
		List<int[]> result = cm.get_comb();
		StringBuilder sb = new StringBuilder();
		for (int[] r : result) {
			for (int i = 0; i < M; i++)
				sb.append(r[i]).append(" ");
			sb.append('\n');
		}
		System.out.println(sb.toString());
		sc.close();
	}
}

class Combination {
	static int[] arr;
	static int[] result;
	static boolean[] visited;
	static List<int[]> final_result;

	Combination(int[] arr, int r) {
		Combination.arr = arr;
		Combination.result = new int[r];
		Combination.visited = new boolean[arr.length];
		final_result = new ArrayList<>();
	}

	List<int[]> get_comb() {
		make(0, 0);
		return final_result;
	}

	void make(int depth, int start) {
		if (depth == result.length) {
			final_result.add(result.clone());
			return;
		}
		int cur = -1;
		for (int i = start; i < arr.length; i++) {
			if (!visited[i]) {
				if (cur == arr[i])
					continue;
				visited[i] = true;
				result[depth] = arr[i];
				make(depth + 1, i + 1);
				visited[i] = false;
				cur = arr[i];
			}
		}
	}
}
