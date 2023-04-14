import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge> {
	int s, e, cost;

	public Edge(int s, int e, int cost) {
		this.s = s;
		this.e = e;
		this.cost = cost;
	}

	@Override
	public int compareTo(Edge target) {
		return this.cost - target.cost;
	}

}

public class Main {
	public static int[] parents;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		char[] sex = new char[N + 1];
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			sex[i] = st.nextToken().charAt(0);
		}

		ArrayList<Edge> Edges = new ArrayList<>();

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int x, y, z;
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			z = Integer.parseInt(st.nextToken());
			if (sex[x] != sex[y])
				Edges.add(new Edge(x, y, z));
		}

		Collections.sort(Edges);

		parents = new int[N + 1];
		for (int i = 0; i <= N; i++)
			parents[i] = i;
		long answer = 0;
		for (Edge e : Edges) {
			if (!check_parent(e.s, e.e)) {
				union(e.s, e.e);
				answer += e.cost;
			}
		}
		for(int i = 1;i<=N;i++) {
			if(find(i)!=1) {
				answer = -1;
				break;
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
