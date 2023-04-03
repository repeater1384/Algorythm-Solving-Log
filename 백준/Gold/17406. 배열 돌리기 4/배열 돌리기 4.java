import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int[][] arr;
	static int[][] orig_arr;
	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { 1, 0, -1, 0 };
	static int N;
	static int M;
	static int K;
	static List<int[]> rotateCmd;
	static int answer;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		orig_arr = new int[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++)
				orig_arr[i][j] = Integer.parseInt(st.nextToken());
		}
		
		rotateCmd = new ArrayList<>();
		for(int i = 0 ;i<K;i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken())-1;
			int c = Integer.parseInt(st.nextToken())-1;
			int s = Integer.parseInt(st.nextToken());
			rotateCmd.add(new int[] {c,r,s});
		}
		answer = Integer.MAX_VALUE;
		
		perm(0,new boolean[K],new int[K]);
		
		System.out.println(answer);
	}
	static void perm(int depth, boolean[] visited, int[] result) {
		if (depth == K) {
			arr = new int[N][M];
			for(int i = 0 ;i<N;i++)
				arr[i] = orig_arr[i].clone();
			for(int i = 0 ;i<K;i++) {
				int[] cur = rotateCmd.get(result[i]);
				rotate(cur[0],cur[1],cur[2]);
			}
			answer = Math.min(answer, getMin());
			return;
		}
		for (int i = 0; i < K; i++) {
			if (!visited[i]) {
				visited[i] = true;
				result[depth] = i;
				perm(depth + 1, visited, result);
				visited[i] = false;
			}
		}
	}
	
	static void rotate(int x, int y, int size) {
		for (int a = 1; a <= size; a++) {
			int sx = x - a, sy = y - a;
			int temp = arr[sy][sx];
			for (int idx = 0;idx<4;idx++) {
				for (int b = 0; b < a * 2; b++) {
					arr[sy][sx] = arr[sy + dy[idx]][sx + dx[idx]];
					sx += dx[idx];
					sy += dy[idx];
				}
			}
			arr[sy][sx + 1] = temp;
		}

	}
	static int getMin() {
		int result = Integer.MAX_VALUE;
		for(int i =0 ;i<N;i++) {
			int sum = 0;
			for(int j = 0 ;j<M;j++) {
				sum += arr[i][j];
			}
			result = Math.min(result, sum);
		}
		return result;
	}

}