
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.lang.StringBuilder;
import java.util.ArrayList;
import java.util.Collections;

class Edge implements Comparable<Edge> {
	int s, e, cost;

	public Edge(int s, int e, int cost) {
		this.s = s;
		this.e = e;
		this.cost = cost;
	}

	@Override
	public int compareTo(Edge target) {
		// TODO Auto-generated method stub
		return this.cost - target.cost;
	}

}

public class Main {
	static int[] parents;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		while (true) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			if (N == 0 && M == 0 && K == 0) {
				break;
			}
			ArrayList<Edge> Edges1 = new ArrayList<>(); // Blue -> 0, Red -> 1, blue use first
			ArrayList<Edge> Edges2 = new ArrayList<>(); // Blue -> 1, Red -> 0, red use first

			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				char color = st.nextToken().charAt(0);
				int s = Integer.parseInt(st.nextToken());
				int e = Integer.parseInt(st.nextToken());
				if (color == 'R') {
					Edges1.add(new Edge(s, e, 1));
					Edges2.add(new Edge(s, e, 0));
				} else {
					Edges1.add(new Edge(s, e, 0));
					Edges2.add(new Edge(s, e, 1));
				}
			}

			parents = new int[N + 1];

			for (int i = 0; i < N + 1; i++)
				parents[i] = i;
			Collections.sort(Edges1);

			int max_blue_use = 0;
			for (Edge e : Edges1) {
				if (!is_same_parent(e.s, e.e)) {
					union(e.s, e.e);
					if (e.cost == 0)
						max_blue_use += 1;
				}
			}

			for (int i = 0; i < N + 1; i++)
				parents[i] = i;
			Collections.sort(Edges2);
			int min_blue_use = 0;
			for (Edge e : Edges2) {
				if (!is_same_parent(e.s, e.e)) {
					union(e.s, e.e);
					if (e.cost == 1)
						min_blue_use += 1;
				}
			}

			System.out.println(min_blue_use <= K && K <= max_blue_use ? 1 : 0);
		}
	}

	static int find(int x) {
		if (x == parents[x])
			return x;
		return parents[x] = find(parents[x]);
	}

	static boolean is_same_parent(int x, int y) {
		return find(x) == find(y);
	}

	static void union(int x, int y) {
		x = find(x);
		y = find(y);
		if (x > y) {
			parents[x] = y;
		} else {
			parents[y] = x;
		}
	}
}
