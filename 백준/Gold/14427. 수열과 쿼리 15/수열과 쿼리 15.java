import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class SegmentTree {
	int[] arr;
	int[] tree;

	SegmentTree(int[] arr, int arr_size) {
		this.arr = arr;
		this.tree = new int[arr_size * 4];
	}

	int init(int start, int end, int node) {
		if (start == end)
			return tree[node] = start;

		int mid = (start + end) / 2;
		return tree[node] = getIdx(init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1));
	}

	int getIdx(int left, int right) {
		return arr[left] == arr[right] ? Math.min(left, right) : arr[left] < arr[right] ? left : right;
	}

	int update(int left, int right, int node, int idx) {
		if (idx < left || right < idx)
			return tree[node];
		if (left==right)
			return tree[node] = idx;
		int mid = (left + right) / 2;
		return tree[node] = getIdx(update(left, mid, node * 2, idx), update(mid + 1, right, node * 2 + 1, idx));

	}
}

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N + 1];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++)
			arr[i] = Integer.parseInt(st.nextToken());

		int M = Integer.parseInt(br.readLine());

		SegmentTree stree = new SegmentTree(arr, N + 1);
		stree.init(1, N, 1);

		StringBuilder sb = new StringBuilder();
		
		while (M-- > 0) {
			st = new StringTokenizer(br.readLine());
			if (Integer.parseInt(st.nextToken()) == 1) {
				// change a to b
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				stree.arr[a] = b;
				stree.update(1, N, 1, a);

			} else {
				sb.append(stree.tree[1]).append("\n");
			}
		}
		System.out.println(sb.toString());
	}

}
