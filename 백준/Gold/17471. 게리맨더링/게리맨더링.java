import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Main {
	static int N;
	static int[] people;
	static boolean[][] adjMatrix;
	static int answer = Integer.MAX_VALUE;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		people = new int[N + 1];
		adjMatrix = new boolean[N + 1][N + 1];

		for (int i = 1; i <= N; i++)
			people[i] = sc.nextInt();
		for (int i = 1; i <= N; i++) {
			int temp = sc.nextInt();
			for (int j = 0; j < temp; j++)
				adjMatrix[i][sc.nextInt()] = true;
		}
		townSplit(0, new boolean[N + 1]);
		System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
		sc.close();
	}

	static void townSplit(int depth, boolean[] selected) {
		if (depth == N) {
			boolean[] townA = new boolean[N + 1];
			boolean[] townB = new boolean[N + 1];
			int check = 0;
			for (int i = 1; i <= N; i++) {
				if (selected[i]) {
					townA[i] = true;
					check++;
				} else {
					townB[i] = true;
				}
			}
			if (check == N || check == 0)
				return;
			if (dfs(townA, townB)) {
				int sumA = 0, sumB = 0;
				for (int i = 1; i <= N; i++) {
					if (townA[i])
						sumA += people[i];
					if (townB[i])
						sumB += people[i];
				}
				answer = Math.min(answer, Math.abs(sumA - sumB));
			}
			return;
		}
		selected[depth + 1] = true;
		townSplit(depth + 1, selected);
		selected[depth + 1] = false;
		townSplit(depth + 1, selected);
	}

	static boolean dfs(boolean[] townA, boolean[] townB) {
		int startA = 0, startB = 0;
		for (int i = 1; i <= N; i++)
			if (townA[i])
				startA = i;
		for (int i = 1; i <= N; i++)
			if (townB[i])
				startB = i;

		Stack<Integer> stack = new Stack<>();
		boolean[] visited = new boolean[N + 1];
		stack.add(startA);
		stack.add(startB);

		while (!stack.isEmpty()) {
			int cur = stack.pop();
			visited[cur] = true;
			for (int next = 1; next <= N; next++) {
				if (adjMatrix[cur][next] && !visited[next]) {
					if ((townA[cur] && townA[next]) || (townB[cur] && townB[next])) {
						visited[next] = true;
						stack.add(next);
					}
				}
			}
		}
		for (int i = 1; i <= N; i++)
			if (!visited[i])
				return false;
		return true;
	}
}