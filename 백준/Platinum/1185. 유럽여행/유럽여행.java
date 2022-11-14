import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Edge implements Comparable<Edge> {
	int s, e, cost;

	Edge(int s, int e, int cost) {
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
	public static int[] parents;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int P = sc.nextInt();
		int[] home_cost = new int[N + 1];

		ArrayList<Edge> Edges = new ArrayList<>();
		int min_home_cost = Integer.MAX_VALUE;
		for (int i = 1; i <= N; i++) {
			home_cost[i] = sc.nextInt();
			min_home_cost = Math.min(home_cost[i], min_home_cost);
		}

		while (P-- > 0) {
			int s, e, r;
			s = sc.nextInt();
			e = sc.nextInt();
			r = sc.nextInt();
			Edges.add(new Edge(s, e, 2 * r + home_cost[s] + home_cost[e]));
		}

		Collections.sort(Edges);

		parents = new int[N + 1];
		for (int i = 0; i <= N; i++)
			parents[i] = i;

		int answer = min_home_cost;
		for (Edge e : Edges) {
			if (!check_parent(e.s, e.e)) {
				union(e.s, e.e);
				answer += e.cost;
			}
		}
		System.out.println(answer);

		// for (Edge e : Edges) {
//			System.out.printf("%d %d %d\n",e.s, e.e, e.cost);
//		}

	}

	public static int find(int x) {
		if (parents[x] == x)
			return x;
		return parents[x] = find(parents[x]);
	}

	public static boolean check_parent(int x, int y) {
		return find(x) == find(y);
	}

	public static void union(int x, int y) {
		int px, py;
		px = find(x);
		py = find(y);
		if (px != py) {
			if (px > py)
				parents[px] = py;
			else
				parents[py] = px;
		}
	}
}
