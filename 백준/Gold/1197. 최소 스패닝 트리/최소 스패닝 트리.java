import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Edge implements Comparable {
	int s, e, cost;

	Edge(int s, int e, int cost) {
		this.s = s;
		this.e = e;
		this.cost = cost;
	}

	@Override
	public int compareTo(Object o) {
		// TODO Auto-generated method stub
		Edge target = (Edge) o;
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
		int E = sc.nextInt();
		ArrayList<Edge> Edges = new ArrayList<>();

		for (int i = 0; i < E; i++) {
			int a, b, w;
			a = sc.nextInt();
			b = sc.nextInt();
			w = sc.nextInt();
			Edges.add(new Edge(a, b, w));
		}

		Collections.sort(Edges);

		parents = new int[V + 1];
		for (int i = 0; i <= V; i++)
			parents[i] = i;
		
		long answer = 0;
		for(Edge e:Edges) {
			if(!check_parent(e.s,e.e)) {
				union(e.s,e.e);
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
