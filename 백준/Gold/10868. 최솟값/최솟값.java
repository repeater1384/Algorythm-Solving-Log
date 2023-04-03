import java.io.*;
import java.util.*;

class SegementTree_MinMax {
	int[] min_tree;
	int[] max_tree;
	int[] arr;

	SegementTree_MinMax(int[] arr, int arr_size) {
		this.arr = arr;
		min_tree = new int[arr_size * 4];
		max_tree = new int[arr_size * 4];
	}

	int min_init(int node, int start, int end) {
		if (start == end)
			return min_tree[node] = arr[start];
		int mid = (start + end) / 2;
		return min_tree[node] = Math.min(min_init(node * 2, start, mid), min_init(node * 2 + 1, mid + 1, end));

	}


	int get_min(int node, int start, int end, int left, int right) {

		if (end < left || right < start)
			return Integer.MAX_VALUE;

		if (left <= start && end <= right)
			return min_tree[node];

		int mid = (start + end) / 2;
		return Math.min(get_min(node * 2, start, mid, left, right), get_min(node * 2 + 1, mid + 1, end, left, right));
	}

}

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[] arr = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		SegementTree_MinMax stree = new SegementTree_MinMax(arr, N + 1);
		stree.min_init(1, 1, N);

		StringBuilder sb = new StringBuilder();
		while (M-- > 0) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int min_value = stree.get_min(1, 1, N, a, b);
			sb.append(min_value).append('\n');
		}
		System.out.println(sb.toString());
	}

}
