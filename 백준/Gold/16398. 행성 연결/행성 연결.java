
//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.io.IOException;
//import java.util.StringTokenizer;
//import java.lang.StringBuilder;
//
//public class Main {
//	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		
//	}
//}
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
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

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		boolean[][] check = new boolean[N][N];
		ArrayList<Edge> Edges = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int cost = sc.nextInt();
				if (!check[i][j] && !check[j][i] && i != j) {
					Edges.add(new Edge(i, j, cost));
					check[i][j] = check[j][i] = true;
				}
			}
		}

		parents = new int[N];
		for (int i = 0; i < N; i++)
			parents[i] = i;
		
		Collections.sort(Edges);
		
		long answer = 0;
		for (Edge e : Edges) {
			if (!is_same_parent(e.s, e.e)) {
				union(e.s, e.e);
				answer += e.cost;
			}
		}
		System.out.println(answer);
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
