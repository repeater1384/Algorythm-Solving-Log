import java.io.*;
import java.util.*;

class SegementTree {
	long[] tree;
	long[] arr;

	SegementTree(long[] arr, int arr_size) {
		this.arr = arr;
		tree = new long[arr_size * 4];
	}

	long init(int node, int start, int end) {
		if (start == end)
			return tree[node] = arr[start];
		int mid = (start + end) / 2;
		return tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end);

	}

	long sum(int node, int start, int end, int left, int right) {

		if (end < left || right < start)
			return 0;

		if (left <= start && end <= right)
			return tree[node];

		int mid = (start + end) / 2;
		return sum(node * 2, start, mid, left, right) + sum(node * 2 + 1, mid + 1, end, left, right);
	}

	void update(int node, int start, int end, int idx, long diff) {
		if (idx < start || end < idx)
			return;
		tree[node] += diff;
		if (start != end) {
			int mid = (start + end) / 2;
			update(node * 2, start, mid, idx, diff);
			update(node * 2 + 1, mid + 1, end, idx, diff);
		}
	}
//	long update(int node, int start, int end, int idx, int change_value) {
//		if (idx < start || end < idx)
//			return tree[node];
//		if (start == idx && start == end)
//			return tree[node] = change_value;
//
//		int mid = (start + end) / 2;
//		return tree[node] = update(node * 2, start, mid, idx, change_value)
//				+ update(node * 2 + 1, mid + 1, end, idx, change_value);
//	}
}

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		long[] arr = new long[N + 1];
		st = new StringTokenizer(br.readLine());

		for (int i = 1; i <= N; i++) {
			arr[i] = Long.parseLong(st.nextToken());
		}

		SegementTree stree = new SegementTree(arr, N + 1);
		stree.init(1, 1, N);

		StringBuilder sb = new StringBuilder();
		while (M-- > 0) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			long result = stree.sum(1, 1, N, Math.min(x, y), Math.max(x, y));
			sb.append(result).append('\n');

			stree.update(1, 1, N, a, b - arr[a]);
			arr[a] = b;
		}

		System.out.println(sb.toString());
	}

}
