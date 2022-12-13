import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] stree;
	static int MAX_SIZE = 65536 + 1;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		stree = new int[MAX_SIZE * 4];
		int[] arr = new int[N];
		long answer = 0;

		for (int i = 0; i < N; i++) {
			// 슬라이딩 윈도우
			arr[i] = Integer.parseInt(br.readLine());
			update(0, MAX_SIZE, 1, arr[i], 1);

			// 빼고 다시 넣으니까, K번 넣은 이후에는 계속 들어감
			if (stree[1] == K) {
				answer += get_median(0, MAX_SIZE, 1, (K + 1) / 2);
				update(0, MAX_SIZE, 1, arr[i - K + 1], -1);
			}
		}

		System.out.println(answer);
	}

	static void update(int start, int end, int Node, int idx, int val) {
		if (idx < start || end < idx)
			return;
		stree[Node] += val;
		if (start == end)
			return;
		int mid = (start + end) / 2;
		update(start, mid, Node * 2, idx, val);
		update(mid + 1, end, Node * 2 + 1, idx, val);
	}

	static int get_median(int start, int end, int Node, int idx) {
		if (start == end)
			return start;
		int mid = (start + end) / 2;
		if (stree[Node * 2] >= idx)
			return get_median(start, mid, Node * 2, idx);
		return get_median(mid + 1, end, Node * 2 + 1, idx - stree[Node * 2]);

	}

}