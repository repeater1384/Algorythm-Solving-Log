import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Edge implements Comparable<Edge> {
	int s, e, cost;

	public Edge(int s, int e, int cost) {
		this.s = s;
		this.e = e;
		this.cost = cost;
	}

	void print() {
		System.out.printf("%d %d %d\n", s, e, cost);
	}

	@Override
	public int compareTo(Edge target) {
		return this.cost - target.cost;
	}

}

public class Main {
	static int N, M;
	static int[][] matrix;
	static boolean[][] visited;
	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static ArrayList<Edge> Edges;
	static int[] parents;

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		M = sc.nextInt();
		matrix = new int[N][M];
		visited = new boolean[N][M];
		Edges = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				matrix[i][j] = sc.nextInt();
			}
		}

		// 섬 넘버링,(땅이 1로 주어지니까 섬 번호는 2부터)
		int num = 2;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (matrix[i][j] == 1) {
					island_numbering(j, i, num++);
				}
			}
		}

		// 각 섬을 잇는 엣지 생성
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (matrix[i][j] >= 2) {
					make_bridge(j, i, matrix[i][j]);
				}
			}
		}

//		for (int[] row : matrix) {
//			for (int j : row) {
//				System.out.printf("%d ", j);
//			}
//			System.out.println();
//		}

		parents = new int[num];
		for (int i = 0; i < num; i++)
			parents[i] = i;
		Collections.sort(Edges);
		int answer = Edges.size() != 0 ? 0 : -1;
		for (Edge e : Edges) {
			if (!check_parents(e.s, e.e)) {
				union(e.s, e.e);
				answer += e.cost;
			}
		}
		for (int i = 2; i < num; i++) {
			if (find_parents(i) != 2) {
				answer = -1;
				break;
			}
		}
		System.out.println(answer);
//		System.out.println("---------------");
//		for (Edge e : Edges)
//			e.print();
	}

	static void island_numbering(int x, int y, int island_num) {
		matrix[y][x] = island_num;
		visited[y][x] = true;

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (0 <= ny && ny < N && 0 <= nx && nx < M) {
				if (!visited[ny][nx] && matrix[ny][nx] == 1) {
					island_numbering(nx, ny, island_num);
				}
			}

		}
	}

	static void make_bridge(int x, int y, int island_num) {
		for (int i = 0; i < 4; i++) {
			int bridge_len = 0;
			int nx = x;
			int ny = y;
			while (true) {
				nx += dx[i];
				ny += dy[i];
				if (0 <= ny && ny < N && 0 <= nx && nx < M) {
					if (matrix[ny][nx] != island_num) {
						if (matrix[ny][nx] == 0) {
							bridge_len++;
							continue;
						} else {
							if (bridge_len > 1) {
								Edges.add(new Edge(island_num, matrix[ny][nx], bridge_len));
								break;

//								Edge temp1 = new Edge(island_num, matrix[ny][nx], bridge_len);
//								Edge temp2 = new Edge(matrix[ny][nx], island_num, bridge_len);
//								if(!Edges.contains(temp1) && !Edges.contains(temp2)) {
//									Edges.add(temp1);
//								}
//								break;
							}
						}
					}
					break;
				}
				break;

			}
		}
	}

	public static int find_parents(int x) {
		if (parents[x] == x)
			return x;
		return parents[x] = find_parents(parents[x]);
	}

	public static boolean check_parents(int x, int y) {
		return find_parents(x) == find_parents(y);
	}

	public static void union(int x, int y) {
		int px, py;
		px = find_parents(x);
		py = find_parents(y);
		if (px != py) {
			if (px > py)
				parents[px] = py;
			else
				parents[py] = px;
		}

	}
}
