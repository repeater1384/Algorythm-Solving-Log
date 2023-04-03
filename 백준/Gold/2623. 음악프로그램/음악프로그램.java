import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		ArrayList<ArrayList<Integer>> adj_list = new ArrayList<>();
		int[] indegree = new int[N + 1];

		for (int i = 0; i < N + 1; i++) {
			adj_list.add(new ArrayList<Integer>());
		}
		while (M-- > 0) {
			int temp = sc.nextInt();
			int start, next;
			start = sc.nextInt();
			for (int i = 0; i < temp - 1; i++) {
				next = sc.nextInt();
				adj_list.get(start).add(next);
				indegree[next]++;
				start = next;
			}
		}

		Queue<Integer> queue = new LinkedList<>();
		for (int i = 1; i <= N; i++) {
			if (indegree[i] == 0)
				queue.add(i);
		}
		ArrayList<Integer> answer = new ArrayList<>();
		while (!queue.isEmpty()) {
			int cur = queue.poll();
			answer.add(cur);

			for (int next : adj_list.get(cur)) {
				if (--indegree[next] == 0) {
					queue.add(next);
				}
			}
		}
		boolean check = true;
		for(int i : indegree) {
			if(i!=0) {
				System.out.println(0);
				check = false;
			}
		}
		if(check) {
			for(int a:answer)System.out.println(a);
		}
	}
}
