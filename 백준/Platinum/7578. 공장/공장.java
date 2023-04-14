import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

class SegmentTree {
	int[] arr;
	long[] tree;

	SegmentTree(int[] arr, int arr_size) {
		this.arr = arr;
		this.tree = new long[arr_size * 4];
	}

	long sum(int start, int end, int node, int left, int right) {
		if (right < start || end < left)
			return 0;
		if (left <= start && end <= right)
			return tree[node];
		int mid = (start + end) / 2;
		return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right);
	}

	long update(int start, int end, int node, int idx, int val) {
		if (idx < start || end < idx)
			return tree[node];
		if (start == end)
			return tree[node] = val;
		int mid = (start + end) / 2;
		return tree[node] = update(start, mid, node * 2, idx, val) + update(mid + 1, end, node * 2 + 1, idx, val);
	}

}

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());

		int[] A = new int[N + 1];
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++)
			A[i] = Integer.parseInt(st.nextToken());

		Map<Integer, Integer> B = new HashMap<>();
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			int b = Integer.parseInt(st.nextToken());
			B.put(b, i);
		}

		long answer = 0;
		SegmentTree stree = new SegmentTree(new int[N + 1], N + 1);

		for (int i = 1; i <= N; i++) {
			int b_idx = B.get(A[i]);

			answer += stree.sum(1, N, 1, b_idx + 1, N);
			stree.update(1, N, 1, b_idx, 1);
		}
		
		System.out.println(answer);
	}

}
