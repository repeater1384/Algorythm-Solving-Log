import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Edge {
	int a, b;

	Edge(int a, int b) {
		this.a = a;
		this.b = b;
	}
}

public class Main {
	static int[] parents;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		ArrayList<Edge> Edges = new ArrayList<>();

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				int cur = sc.nextInt();
				if (cur == 1) {
					Edges.add(new Edge(i, j));
				}
			}
		}
		parents = new int[N + 1];
		for (int i = 0; i < N + 1; i++) {
			parents[i] = i;
		}
		for (Edge e : Edges) {
			union(e.a, e.b);
		}
		
		int[] go = new int[M];
		for(int i = 0 ;i<M;i++) {
			go[i] = sc.nextInt();
		}
		
		int temp = parents[go[0]];
		boolean can_go = true;
		for(int g:go) {
			if(temp != parents[g]) {
				can_go = false;
				break;
			}
		}
		System.out.println(can_go ? "YES" : "NO");
	}

	static int find_parent(int x) {
		if (parents[x] == x)
			return x;
		return parents[x] = find_parent(parents[x]);
	}

	static void union(int x, int y) {
		x = find_parent(x);
		y = find_parent(y);
		if (x > y) {
			parents[x] = y;
		} else {
			parents[y] = x;
		}
	}
}
