import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int M, N, K, answer;
	static int[][] arr, farm;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		while (T-- > 0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			
			arr = new int[N][M];
			while(K-->0) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken()); 
				int y = Integer.parseInt(st.nextToken());
				arr[y][x] = 1;
			}
			
			answer = 0;
			for(int i = 0 ;i<N;i++) {
				for(int j = 0 ;j<M;j++) {
					if(arr[i][j]==1) {
						bfs(i,j);
						answer++;
					}
				}
			}
			System.out.println(answer);
		}
	}

	private static void bfs(int si, int sj) {
		int[] di = {1,0,-1,0};
		int[] dj = {0,1,0,-1};
		
		Queue<int[]> queue = new LinkedList<>();
		arr[si][sj] = 0;
		queue.add(new int[] {si,sj});
		while(!queue.isEmpty()) {
			int[] cur = queue.poll();
			int ci = cur[0];
			int cj = cur[1];
			for(int k = 0 ; k<4;k++) {
				int ni = ci+di[k];
				int nj = cj+dj[k];
				if(0<=ni && ni<N && 0<=nj && nj<M && arr[ni][nj]==1) {
					arr[ni][nj]=0;
					queue.add(new int[] {ni,nj});
				}
			}
		}
	}
}