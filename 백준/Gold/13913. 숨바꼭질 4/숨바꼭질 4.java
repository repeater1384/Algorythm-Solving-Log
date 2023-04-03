import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		if (K < N) {
			System.out.println(N-K);
			for (int i = N; i >= K; i--)
				System.out.print(i + " ");
			System.exit(0);
		}
		List<Integer>[] dp = new ArrayList[100001];
		boolean[] visited = new boolean[100001];

		Queue<Object[]> queue = new ArrayDeque<>();
		ArrayList<Integer> temp = new ArrayList<>();
		temp.add(N);
		queue.add(new Object[] { N, temp });
		visited[N] = true;

		while (!queue.isEmpty()) {
			Object[] cur = queue.poll();
			int pos = (int) cur[0];
			ArrayList<Integer> path = (ArrayList<Integer>) cur[1];
			if (pos == K) {
				System.out.println(path.size() - 1);
				for (Integer i : path) {
					System.out.print(i + " ");
				}
				break;
			}

			if (pos * 2 <= 100000 && !visited[pos * 2]) {
				ArrayList<Integer> nextPath = (ArrayList<Integer>) path.clone();
				nextPath.add(pos * 2);
				queue.add(new Object[] { pos * 2, nextPath });
				visited[pos * 2] = true;
			}
			if (pos + 1 <= 100000 && !visited[pos + 1]) {
				ArrayList<Integer> nextPath = (ArrayList<Integer>) path.clone();
				nextPath.add(pos + 1);
				queue.add(new Object[] { pos + 1, nextPath });
				visited[pos + 1] = true;
			}

			if (pos - 1 >= 0 && !visited[pos - 1]) {
				ArrayList<Integer> nextPath = (ArrayList<Integer>) path.clone();
				nextPath.add(pos - 1);
				queue.add(new Object[] { pos - 1, nextPath });
				visited[pos - 1] = true;
			}
		}
		sc.close();
	}
}