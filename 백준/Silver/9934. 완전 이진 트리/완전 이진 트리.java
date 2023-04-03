import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
	static List<ArrayList<Integer>> answer;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int K = sc.nextInt();
		int size = (int) Math.pow(2, K) - 1;
		int[] arr = new int[size];
		for (int i = 0; i < size; i++)
			arr[i] = sc.nextInt();

		answer = new ArrayList<>();
		for (int i = 0; i < K; i++)
			answer.add(new ArrayList<>());

		dfs(0, arr);
		for (int i = 0; i < K; i++) {
			for (int e : answer.get(i))
				System.out.print(e + " ");
			System.out.println();
		}

		sc.close();
	}

	static void dfs(int level, int[] cur) {
		if (cur.length == 0) {
			return;
		}

		int mid_idx = cur.length / 2;
		int root = cur[mid_idx];
		answer.get(level).add(root);

		int[] left = Arrays.copyOf(cur, mid_idx);
		dfs(level + 1, left);
		int[] right = Arrays.copyOfRange(cur, mid_idx + 1, cur.length);
		dfs(level + 1, right);

	}

}