import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		PriorityQueue<Integer> heap = new PriorityQueue<>(new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				return Math.abs(o1) == Math.abs(o2) ? o1 - o2 : Math.abs(o1) - Math.abs(o2);
			}

		});

		int N = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();

		while (N-- > 0) {
			int cur = Integer.parseInt(br.readLine());
			if (cur == 0)
				sb.append(heap.isEmpty() ? 0 : heap.poll()).append('\n');
			else
				heap.add(cur);

		}
		
		System.out.println(sb.toString());
	}

}