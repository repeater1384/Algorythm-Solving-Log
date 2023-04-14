import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static List<List<int[]>> adjList;
	static long[] dist;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		adjList = new ArrayList<>();
		for (int i = 0; i < N + 1; i++) {
			adjList.add(new ArrayList<>());
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			adjList.get(A).add(new int[] { B, C });
		}

		dist = new long[N + 1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		boolean isNegative = bellman_ford(1);
		if (isNegative) {
			System.out.println(-1);
		} else {
			for (int i = 2; i < N + 1; i++)
				System.out.println(dist[i] == Integer.MAX_VALUE ? -1 : dist[i]);
		}
	}

	static boolean bellman_ford(int start) {
		dist[start] = 0;

		// N-1 번 반복
		int loop = N - 1;
		while (loop-- > 0) {
			for (int i = 1; i < N + 1; i++) {
				if (dist[i] == Integer.MAX_VALUE)
					continue;

				for (int[] edge : adjList.get(i)) {
					int j = edge[0];
					int cost = edge[1];
					dist[j] = Math.min(dist[j], dist[i] + cost);
				}
			}
		}

		// N번째 반복에서 갱신되면 음의 사이클 존재
		for (int i = 1; i < N + 1; i++) {
			if (dist[i] == Integer.MAX_VALUE)
				continue;

			for (int[] edge : adjList.get(i)) {
				int j = edge[0];
				int cost = edge[1];
				if (dist[j] > dist[i] + cost)
					return true;
			}
		}
		return false;
	}
}