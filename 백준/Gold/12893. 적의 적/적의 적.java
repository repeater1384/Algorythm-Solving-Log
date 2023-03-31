import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		List<Integer>[] adjList = new ArrayList[V + 1];
		for (int i = 1; i <= V; i++)
			adjList[i] = new ArrayList<Integer>();
		while (E-- > 0) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			adjList[a].add(b);
			adjList[b].add(a);
		}

		// bfs
		Queue<int[]> queue = new LinkedList<>();
		int[] visited = new int[V + 1];
		boolean check = true;
		outer : for (int startV = 1; startV <= V; startV++) {
			if (visited[startV] != 0)
				continue;
			queue.add(new int[] { startV, 1 });
			visited[startV] = 1;

			while (!queue.isEmpty()) {
				int[] cur = queue.poll();
				int curV = cur[0];
				int curColor = cur[1];
				int otherColor = curColor == 1 ? -1 : 1;
				for (int nextV : adjList[curV]) {
					if (visited[nextV] == 0) {
						visited[nextV] = otherColor;
						queue.add(new int[] { nextV, otherColor });
					} else if (visited[nextV] == curColor) {
						check = false;
						break outer;
					}
				}
			}
		}

		System.out.println(check ? 1 : 0);
	}

}