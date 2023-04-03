import java.util.Scanner;

public class Main {
	static int[] parents;

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		parents = new int[N + 1];
		for (int i = 0; i < N + 1; i++)
			parents[i] = i;

		for (int i = 0; i < M; i++) {
			int op = sc.nextInt();
			int A = sc.nextInt();
			int B = sc.nextInt();

			if (op == 0) {
				union(A, B);
			} else {
				System.out.println(is_same_parent(A, B) ? "YES" : "NO");
			}
		}

	}

	public static int find_parent(int x) {
		if (parents[x] == x)
			return x;
		return parents[x] = find_parent(parents[x]);
	}

	public static boolean is_same_parent(int x, int y) {
		return find_parent(x) == find_parent(y);
	}

	public static void union(int x, int y) {
		x = find_parent(x);
		y = find_parent(y);
		if (x > y) {
			parents[x] = y;
		} else {
			parents[y] = x;
		}
	}

}