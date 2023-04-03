import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;

class planet {
	int x, y, z, num;

	planet(int x, int y, int z, int num) {
		this.x = x;
		this.y = y;
		this.z = z;
		this.num = num;
	}

	long get_distance(planet p) {
		return Math.min(Math.min(Math.abs(p.x - this.x), Math.abs(p.y - this.y)), Math.abs(p.z - this.z));
	}
}

class Edge implements Comparable {
	int s, e;
	long dis;

	Edge(int s, int e, long dis) {
		this.s = s;
		this.e = e;
		this.dis = dis;
	}

	@Override
	public int compareTo(Object o) {
		// TODO Auto-generated method stub
		Edge target = (Edge) o;
		if (this.dis < target.dis)
			return -1;
		else if (this.dis > target.dis)
			return 1;
		return 0;
	}

}

public class Main {
	public static int[] parents;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		ArrayList<Edge> Edges = new ArrayList<>();
		planet[] planets = new planet[N];

		for (int i = 0; i < N; i++) {
			int x, y, z;
			x = sc.nextInt();
			y = sc.nextInt();
			z = sc.nextInt();
			planets[i] = new planet(x, y, z, i);
		}

		Arrays.sort(planets, (p1, p2) -> p1.x - p2.x);
		for (int i = 0; i < N - 1; i++) {
			Edges.add(new Edge(planets[i].num, planets[i + 1].num, Math.abs(planets[i + 1].x - planets[i].x)));
		}

		Arrays.sort(planets, (p1, p2) -> p1.y - p2.y);
		for (int i = 0; i < N - 1; i++) {
			Edges.add(new Edge(planets[i].num, planets[i + 1].num, Math.abs(planets[i + 1].y - planets[i].y)));
		}

		Arrays.sort(planets, (p1, p2) -> p1.z - p2.z);
		for (int i = 0; i < N - 1; i++) {
			Edges.add(new Edge(planets[i].num, planets[i + 1].num, Math.abs(planets[i + 1].z - planets[i].z)));
		}

		parents = new int[N];
		for (int i = 0; i < N; i++)
			parents[i] = i;

		Collections.sort(Edges);
		
		long answer = 0;
		for (Edge e : Edges) {
			if (!check_parent(e.s, e.e)) {
				union(e.s, e.e);
				answer += e.dis;
			}
		}
		System.out.println(answer);

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
