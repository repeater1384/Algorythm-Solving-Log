import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge> {
	int to, weight;

	public Edge(int to, int weight) {
		super();
		this.to = to;
		this.weight = weight;
	}

	@Override
	public int compareTo(Edge o) {
		return Integer.compare(this.weight, o.weight);
	}

}

public class Main {
	static int N;
	static List<Edge>[] adjList;

	public static void main(String[] args) throws IOException {
		StringTokenizer st = null;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int V = Integer.parseInt(st.nextToken());

		adjList = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			adjList[i] = new ArrayList<Edge>();
		}

		while (V-- > 0) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			adjList[a].add(new Edge(b, cost));
			adjList[b].add(new Edge(a, cost));
		}

		// drinkCome[i] -> i번째 지점까지 오는데 소요되는 시간.
		long[] drinkCome = new long[10];
		Arrays.fill(drinkCome, Long.MAX_VALUE);
		drinkCome[0] = 0;

		// 아줌마가 오는 지점들
		int[] drinkNode = new int[10];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 10; i++) {
			drinkNode[i] = Integer.parseInt(st.nextToken());
		}

		int cur = drinkNode[0];
		int curIdx = 0;
		for (int i = 1; i < 10; i++) {
			int next = drinkNode[i];
			int minCost = dijkstra(cur)[next];

			// cur에서 next로 못가는 상황. cur은 유지하고 next만 새로 받아서 다시 계산.
			if (minCost == Integer.MAX_VALUE) {
				continue;
			}

			drinkCome[i] = minCost + drinkCome[curIdx];
			cur = next;
			curIdx = i;
		}

		int myNode = Integer.parseInt(br.readLine());
		int[] myPath = dijkstra(myNode);
		int answer = Integer.MAX_VALUE;

		for (int i = 0; i < 10; i++) {
			// 내가 i번째 지점으로 가는 시간과 야쿠르트 아줌마가 오는 시간이랑 비교.
			// 아줌마가 i번째 지점으로 올수 있고, 내가 더 빨리 도착하면 answer 갱신.
			int curDrinkNode = drinkNode[i];
			if (drinkCome[i] != Long.MAX_VALUE && myPath[curDrinkNode] <= drinkCome[i])
				answer = Math.min(answer, curDrinkNode);

		}

		System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);

	}

	static int[] dijkstra(int start) {
		// path[a] -> start부터 a까지 가는데 소요되는 최소비용
		// start부터 시작하는 각 정점까지의 최소비용을 path에 담아 return.

		int path[] = new int[N + 1];
		Arrays.fill(path, Integer.MAX_VALUE);

		PriorityQueue<Edge> pq = new PriorityQueue<>();

		pq.add(new Edge(start, 0));
		path[start] = 0;

		while (!pq.isEmpty()) {
			Edge cur = pq.poll();

			if (cur.weight > path[cur.to])
				continue;

			for (Edge next : adjList[cur.to]) {
				int cost = path[cur.to] + next.weight;

				if (path[next.to] > cost) {
					path[next.to] = cost;
					pq.add(new Edge(next.to, cost));
				}
			}
		}
		return path;
	}
}