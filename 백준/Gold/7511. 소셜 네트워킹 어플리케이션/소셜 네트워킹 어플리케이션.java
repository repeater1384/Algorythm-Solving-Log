import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] parents;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringTokenizer st = null;
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= T; tc++) {

			int N = Integer.parseInt(br.readLine());
			parents = new int[N + 1];
			for (int i = 0; i <= N; i++)
				parents[i] = i;
			
			int K = Integer.parseInt(br.readLine());
			while (K-- > 0) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				if (!is_same_parent(a, b))
					union(a, b);
			}
			int M = Integer.parseInt(br.readLine());
			sb.append("Scenario " + tc + ":").append('\n');
			while (M-- > 0) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				sb.append(is_same_parent(a, b) ? 1 : 0).append('\n');
			}
			
			if (tc < T)
				sb.append('\n');
		}
		System.out.print(sb.toString());
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