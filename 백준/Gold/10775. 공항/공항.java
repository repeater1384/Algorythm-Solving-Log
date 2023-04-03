import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int[] parents;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		parents = new int[N + 1];
		for (int i = 0; i <= N; i++)
			parents[i] = i;
		int P = Integer.parseInt(br.readLine());
		int answer = 0;
		while (P-- > 0) {
			int cur = Integer.parseInt(br.readLine());
			while (true) {
				if (find_parent(cur) == 0) {
					System.out.println(answer);
					System.exit(0);
				}
				if (find_parent(cur) == cur) {
					union(cur, cur - 1);
					break;
				}
				cur = find_parent(cur);
			}
			answer++;
		}
		System.out.println(answer);
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