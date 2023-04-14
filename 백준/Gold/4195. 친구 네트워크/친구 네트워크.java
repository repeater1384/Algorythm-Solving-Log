import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;

class Edge {
	int a, b;

	Edge(int a, int b) {
		this.a = a;
		this.b = b;
	}
}

public class Main {
	static int[] parents;
	static int[] counts;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		while (T-- > 0) {
			HashMap<String, Integer> map = new HashMap<>();
			int F = sc.nextInt();
			parents = new int[F * 2];
			counts = new int[F * 2];

			for (int i = 0; i < F * 2; i++) {
				parents[i] = i;
				counts[i] = 1;
			}

			int map_idx = 0;
			for (int i = 0; i < F; i++) {
				String a = sc.next();
				String b = sc.next();
				if (!map.containsKey(a)) {
					map.put(a, map_idx++);
				}
				if (!map.containsKey(b)) {
					map.put(b, map_idx++);
				}
				System.out.println(union_N_getCount(map.get(a), map.get(b)));
			}

		}
	}

	static int find_parent(int x) {
		if (parents[x] == x)
			return x;
		return parents[x] = find_parent(parents[x]);
	}

	static boolean is_same_parent(int x, int y) {
		return find_parent(x) == find_parent(y);
	}

	static int union_N_getCount(int x, int y) {
		x = find_parent(x);
		y = find_parent(y);
		if (x == y)
			return counts[x];

		if (x > y) {
			parents[x] = y;
			counts[y] += counts[x];
			return counts[y];
		} else {
			parents[y] = x;
			counts[x] += counts[y];
			return counts[x];
		}
	}
}
