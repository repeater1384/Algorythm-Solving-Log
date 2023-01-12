import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        List<Integer>[] adjList = new ArrayList[N + 1];
        int[] costs = new int[N + 1];
        int[] inDegree = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            adjList[i] = new ArrayList<>();
        }
        for (int i = 1; i <= N; i++) {
            int cost = sc.nextInt();
            costs[i] = cost;
            while (true) {
                int need = sc.nextInt();
                if (need == -1) {
                    break;
                }
                adjList[need].add(i);
                inDegree[i]++;
            }
        }
        Queue<Integer> queue = new LinkedList<>();
        int[] result = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            if (inDegree[i] == 0) {
                queue.add(i);
            }
        }
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            for (int next :
                    adjList[cur]) {
                inDegree[next]--;
                if (inDegree[next] == 0) {
                    queue.add(next);
                }
                result[next] = Math.max(result[next], result[cur] + costs[cur]);
            }
        }

        for (int i = 1; i <= N; i++) {
            System.out.println(result[i] + costs[i]);
        }
    }
}