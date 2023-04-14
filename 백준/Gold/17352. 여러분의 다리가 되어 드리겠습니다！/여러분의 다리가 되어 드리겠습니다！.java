import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] parents;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		int N = Integer.parseInt(br.readLine());
		parents = new int[N + 1];
		for (int i = 0; i <= N; i++)
			parents[i] = i;

		for (int i = 0; i < N - 2; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			if (!is_same_parent(a, b))
				union(a, b);
		}

		for (int i = 2; i <= N; i++) {
			if (!is_same_parent(1, i)) {
				System.out.println(1 + " " + i);
				break;
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