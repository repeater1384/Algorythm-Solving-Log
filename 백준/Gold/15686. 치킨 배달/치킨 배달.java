import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Node {
	int x;
	int y;

	public Node(int x, int y) {
		super();
		this.x = x;
		this.y = y;
	}

}

public class Main {
	static int N, M;
	static int[][] arr;
	static Node[] home;
	static int home_size;
	static Node[] chicken;
	static int chicken_size;
	static int answer;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		arr = new int[N][N];
		home = new Node[N * 2];
		chicken = new Node[13];
		home_size = chicken_size = 0;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 1)
					home[home_size++] = new Node(j, i);
				if (arr[i][j] == 2)
					chicken[chicken_size++] = new Node(j, i);
			}
		}
		answer = Integer.MAX_VALUE;
		comb(0, 0, new int[M]);
		System.out.println(answer);
	}

	static void comb(int depth, int start, int[] selected) {
		if (depth == M) {
			int cur_dis = 0;
			for (int h = 0; h < home_size; h++) {
				Node cur_home = home[h];
				int min_dis = Integer.MAX_VALUE;
				for (int i = 0; i < M; i++) {
					Node cur_chicken = chicken[selected[i]];
					min_dis = Math.min(min_dis, get_dis(cur_home, cur_chicken));
				}
				cur_dis += min_dis;
			}
			answer = Math.min(answer, cur_dis);
			return;
		}
		for (int i = start; i < chicken_size; i++) {
			selected[depth] = i;
			comb(depth + 1, i + 1, selected);
		}
	}

	static int get_dis(Node home, Node chicken) {
		return Math.abs(home.x - chicken.x) + Math.abs(home.y - chicken.y);
	}

}