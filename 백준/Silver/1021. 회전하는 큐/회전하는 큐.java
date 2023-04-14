import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] target = new int[M];
		for (int i = 0; i < M; i++)
			target[i] = sc.nextInt();

		int answer = 0;

		LinkedList<Integer> queue = new LinkedList<>();
		for (int i = 1; i <= N; i++)
			queue.add(i);
		for (int t : target) {
			int idx = -1;
			for (int i = 0; i < queue.size(); i++) {
				if (queue.get(i) == t) {
					idx = i;
					break;
				}
			}

			if (idx <= (queue.size() - 1) / 2) {
				while (queue.get(0) != t) {
					queue.add(queue.poll());
					answer++;
				}
				queue.poll();
			} else {
				while (queue.get(0) != t) {
					queue.addFirst(queue.pollLast());
					answer++;
				}
				queue.poll();
			}
		}
		System.out.println(answer);
	}
}