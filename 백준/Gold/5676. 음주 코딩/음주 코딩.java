import java.io.*;
import java.util.*;

class SegementTree {
	int[] arr;
	int[] tree;

	SegementTree(int[] arr, int arr_size) {
		tree = new int[arr_size * 4];
		this.arr = arr;
	}

	int init(int node, int start, int end) {
		if (start == end)
			return tree[node] = arr[start];
		int mid = (start + end) / 2;
		return tree[node] = init(node * 2, start, mid) * init(node * 2 + 1, mid + 1, end);
	}

	int get_mul(int node, int start, int end, int left, int right) {
		if (end < left || right < start)
			return 1;
		if (left <= start && end <= right)
			return tree[node];
		int mid = (start + end) / 2;
		return get_mul(node * 2, start, mid, left, right) * get_mul(node * 2 + 1, mid + 1, end, left, right);
	}

	int update(int node, int start, int end, int idx, int val) {

		if (end < idx || idx < start)
			return tree[node];
		if (start == end)
			return tree[node] = val;
		int mid = (start + end) / 2;
		return tree[node] = update(node * 2, start, mid, idx, val) * update(node * 2 + 1, mid + 1, end, idx, val);
	}
}

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			String check = br.readLine();
			if (check == null)
				break;
			StringTokenizer st = new StringTokenizer(check);

			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			int[] arr = new int[N + 1];
			for (int i = 1; i <= N; i++) {
				arr[i] = convert_num(Integer.parseInt(st.nextToken()));
			}

			SegementTree stree = new SegementTree(arr, N + 1);
			stree.init(1, 1, N);

			StringBuilder sb = new StringBuilder();

			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				char op = st.nextToken().charAt(0);
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				if (op == 'C') {
					b = convert_num(b);
					stree.arr[a] = b;
					stree.update(1, 1, N, a, b);
				} else if (op == 'P') {
					int mul = stree.get_mul(1, 1, N, a, b);
					sb.append(convert_num2char(mul));
				}
			}
			System.out.println(sb.toString());
		}
	}

	static int convert_num(int num) {
		return num == 0 ? 0 : num > 0 ? 1 : -1;
	}

	static char convert_num2char(int num) {
		return num == 0 ? '0' : num > 0 ? '+' : '-';
	}
}
