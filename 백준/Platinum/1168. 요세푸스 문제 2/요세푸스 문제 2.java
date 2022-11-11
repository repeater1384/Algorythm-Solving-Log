import java.util.Scanner;

class SegmentTree {
	int tree[];

	SegmentTree(int N) {
		tree = new int[N * 4];
	}

	int init(int start, int end, int node) {
		// 리프노드를 제외한 노드는 해당 구간에 몇개의 원소가 있는지를 나타냄
		if (start == end)
			return tree[node] = 1;

		int mid = (start + end) / 2;
		return tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1);
	}

	int find_order(int start, int end, int node, int order) {
		if (start == end)
			return start;
		int mid = (start + end) / 2;
		// 왼쪽으로 탐색하였을때 order이 이미 들어있으면.
		if (order <= tree[node * 2])
			return find_order(start, mid, node * 2, order);
		// 왼쪽만으로는 order번째 순서가 안나오면, 오른쪽에서 order - tree[node*2]를 찾음.
		return find_order(mid + 1, end, node * 2 + 1, order - tree[node * 2]);
	}

	int delete(int start, int end, int node, int order) {
		// order을 제거하면서 모든 노드를 수정
		tree[node]--;
		if (start == end)
			return 0;
		int mid = (start + end) / 2;

		// 지울게 왼쪽에 있으면.
		if (order <= mid)
			return delete(start, mid, node * 2, order);
		// 지울게 오른쪽에 있으면.
		return delete(mid + 1, end, node * 2 + 1, order);
	}
}

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		StringBuilder answer = new StringBuilder();
		answer.append("<");

		SegmentTree stree = new SegmentTree(N);
		stree.init(1, N, 1);
		int idx = 1;
		for (int time = 0; time < N; time++) {
			int left_people = N - time;
			idx = (idx + K - 1) % left_people;
			idx = (idx == 0) ? left_people : idx;

			// order -> idx번째 해당하는 원소의 위치
			int order = stree.find_order(1, N, 1, idx);
			
			answer.append(order);
			if (time < N - 1)
				answer.append(", ");
			
			stree.delete(1, N, 1, order);

		}
		System.out.println(answer.append(">").toString());
		sc.close();
	}

}
