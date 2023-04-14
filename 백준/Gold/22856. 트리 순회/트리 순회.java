import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Node {
	int left;
	int right;

	public Node(int left, int right) {
		this.left = left;
		this.right = right;
	}

}

public class Main {
	static Node[] arr;
	static ArrayList<Integer> inorder_result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		arr = new Node[N + 1];
		inorder_result = new ArrayList<>();
		int answer = 0;
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			if (b != -1)
				answer += 2;
			if (c != -1)
				answer += 2;
			arr[a] = new Node(b, c);
		}

		inorder1(1);
		int target = inorder_result.get(N - 1);
		int cur_idx = 1;
		while (true) {
			if (cur_idx == target) {
				System.out.println(answer);
				break;
			}
			answer--;
			cur_idx = arr[cur_idx].right;

		}
	}

	static void inorder1(int idx) {
		Node cur = arr[idx];
		if (cur.left != -1)
			inorder1(cur.left);
		inorder_result.add(idx);
		if (cur.right != -1)
			inorder1(cur.right);
	}

}