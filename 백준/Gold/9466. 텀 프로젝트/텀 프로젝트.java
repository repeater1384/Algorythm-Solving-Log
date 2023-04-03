import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	static int[] arr;
	static int team_count = 0;
	static boolean[] visited;
	static boolean[] finished;

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		while (T-- > 0) {
			int N = Integer.parseInt(br.readLine());
			arr = new int[N + 1];
			visited = new boolean[N + 1];
			finished = new boolean[N + 1];
			team_count = 0;

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());

			}
			for (int i = 1; i <= N; i++) {
				dfs(i);
			}
			System.out.println(N - team_count);
		}

	}

	static void dfs(int cur) {
		if (visited[cur])
			return;

		visited[cur] = true;
		int next = arr[cur];

		if (!visited[next])
			dfs(next);
		else {
			if (!finished[next]) {
				team_count++;
				while (next != cur) {
					next = arr[next];
					team_count++;
				}
			}
		}
		finished[cur] = true;
	}
}