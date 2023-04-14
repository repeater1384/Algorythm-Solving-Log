import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Edge implements Comparable<Edge> {
	int s, e;
	double cost;

	Edge(int s, int e, double cost) {
		this.s = s;
		this.e = e;
		this.cost = cost;
	}

	@Override
	public int compareTo(Edge target) {
		// TODO Auto-generated method stub
		if (this.cost < target.cost)
			return -1;
		else if (this.cost > target.cost)
			return 1;
		return 0;
	}

}

public class Main {
	public static int[] parents;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int V = sc.nextInt();
		int M = sc.nextInt();
		ArrayList<Edge> Edges = new ArrayList<>();
		long[][] pos = new long[V][2];

		for (int i = 0; i < V; i++) {
			int x, y;
			x = sc.nextInt();
			y = sc.nextInt();
			pos[i][0] = x;
			pos[i][1] = y;
		}

		for (int i = 0; i < V - 1; i++) {
			for (int j = i + 1; j < V; j++) {
				long ix, iy, jx, jy;
				double cost;
				ix = pos[i][0];
				iy = pos[i][1];
				jx = pos[j][0];
				jy = pos[j][1];
				cost = Math.sqrt((jx - ix) * (jx - ix) + (jy - iy) * (jy - iy));
				Edges.add(new Edge(i, j, cost));
			}

		}

		

		parents = new int[V];
		for (int i = 0; i < V; i++)
			parents[i] = i;

		for (int i = 0; i < M; i++) {
			int x, y;
			x = sc.nextInt() - 1;
			y = sc.nextInt() - 1;
			Edges.add(new Edge(x,y,0));
//			union(x, y);
		}
		Collections.sort(Edges);
		double answer = 0;
		for (Edge e : Edges) {
			if (!check_parent(e.s, e.e)) {
				union(e.s, e.e);
				answer += e.cost;
			}
		}
		System.out.println(String.format("%.2f", answer));

//		for (Edge e : Edges) {
//			System.out.printf("%d %d %f\n", e.s, e.e, e.cost);
//		}
//		for (int e : parents)
//			System.out.println(e);

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
