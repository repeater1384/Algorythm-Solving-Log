import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class SegmentTree {
	int[] tree;
	int[] arr;

	SegmentTree(int[] arr, int size) {
		this.tree = new int[size * 4];
		this.arr = arr;
	}

	int init(int start, int end, int Node) {
		if (start == end)
			return tree[Node] = start;
		int mid = (start + end) / 2;
		int left_idx = init(start, mid, Node * 2);
		int right_idx = init(mid + 1, end, Node * 2 + 1);
		return tree[Node] = arr[left_idx] < arr[right_idx] ? left_idx : right_idx;

	}

	int get_idx(int start, int end, int left, int right, int Node) {
		if (end < left || right < start)
			return -1;
		if (left <= start && end <= right)
			return tree[Node];
		int mid = (start + end) / 2;

		int left_idx = get_idx(start, mid, left, right, Node * 2);
		int right_idx = get_idx(mid + 1, end, left, right, Node * 2 + 1);
		if (left_idx == -1)
			return right_idx;
		if (right_idx == -1)
			return left_idx;
		return arr[left_idx] < arr[right_idx] ? left_idx : right_idx;
	}
}

public class Main {

	static long answer;
	static SegmentTree stree;
	static int N;
	static int[] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			if (N == 0)
				break;

			answer = 0;
			arr = new int[N + 1];
			for (int i = 1; i <= N; i++)
				arr[i] = Integer.parseInt(st.nextToken());

			stree = new SegmentTree(arr, N);
			stree.init(1, N, 1);
			main_solve(1, N);
			System.out.println(answer);
		}
	}

	static void main_solve(int left, int right) {
		if (left > right)
			return;
		int idx = stree.get_idx(1, N, left, right, 1);
		answer = Math.max(answer, (long)arr[idx] * (right - left + 1));

		main_solve(left, idx - 1);
		main_solve(idx + 1, right);
	}

}