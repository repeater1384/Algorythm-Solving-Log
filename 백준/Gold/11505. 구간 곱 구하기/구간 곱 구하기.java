import java.io.*;
import java.util.*;

class SegementTree {
	int[] arr;
	long[] tree;
	final int MOD = 1000000007;

	SegementTree(int[] arr, int arr_size) {
		tree = new long[arr_size * 4];
		this.arr = arr;
	}

	long init(int node, int start, int end) {
		if (start == end)
			return tree[node] = arr[start];
		int mid = (start + end) / 2;
		return tree[node] = (init(node * 2, start, mid) * init(node * 2 + 1, mid + 1, end)) % MOD;
	}

	long get_mul(int node, int start, int end, int left, int right) {
		if (end < left || right < start)
			return 1;
		if (left <= start && end <= right)
			return tree[node];
		int mid = (start + end) / 2;
		return (get_mul(node * 2, start, mid, left, right) * get_mul(node * 2 + 1, mid + 1, end, left, right)) % MOD;
	}

	long update(int node, int start, int end, int idx, int diff) {
		arr[idx] = diff;
		if (end < idx || idx < start)
			return tree[node];
		if (start == end)
			return tree[node] = diff;
		int mid = (start + end) / 2;
		return tree[node] = (update(node * 2, start, mid, idx, diff) * update(node * 2 + 1, mid + 1, end, idx, diff))
				% MOD;
	}
}

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		int[] arr = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		SegementTree stree = new SegementTree(arr, N + 1);
		stree.init(1, 1, N);

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < M + K; i++) {
			st = new StringTokenizer(br.readLine());
			int op = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			if (op == 1) {
				stree.update(1, 1, N, a, b);
			} else if (op == 2) {
				int answer = (int) stree.get_mul(1, 1, N, a, b);
				sb.append(answer).append('\n');
			}
		}
		System.out.println(sb.toString());
	}

}
