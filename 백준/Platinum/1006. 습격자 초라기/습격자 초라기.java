import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int W;
	static int[] in_enemy;
	static int[] out_enemy;
	static int[] in;
	static int[] out;
	static int[] both;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		while (T-- > 0) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());

			in_enemy = new int[N];
			out_enemy = new int[N];

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++)
				in_enemy[i] = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++)
				out_enemy[i] = Integer.parseInt(st.nextToken());

			in = new int[N]; // in_enemy는 N, out_enemy는 N-1까지
			out = new int[N]; // in_enemy는 N-1, out_enemy는 N까지
			both = new int[N + 1]; // in_enemy는 N-1, out_enemy는 N-1까지

			
			int answer = Integer.MAX_VALUE;
			// #1 : 처음과 끝이 걸치지 않는 경우
			in[0] = out[0] = 1;
			both[0] = 0;
			fill_dp(0);
			answer = Math.min(answer, both[N]);
			if(N>1) {
				// #2 : 안쪽만 겹치는 경우
				if(in_enemy[0]+in_enemy[N-1]<=W) {
					in[1] = 2;
					out[1] = out_enemy[0]+out_enemy[1]<=W?1:2;
					both[1] = 1;
					fill_dp(1);
					answer = Math.min(answer, out[N-1]+1);
				}
				// #3 : 바깥쪽만 겹치는 경우
				if(out_enemy[0]+out_enemy[N-1]<=W) {
					in[1] = in_enemy[0]+in_enemy[1]<=W?1:2;
					out[1] = 2;
					both[1] = 1;
					fill_dp(1);
					answer = Math.min(answer, in[N-1]+1);
				}
				// #4 : 안쪽과 바깥쪽 모두 겹치는 경우
				if(in_enemy[0]+in_enemy[N-1]<=W && out_enemy[0]+out_enemy[N-1]<=W) {
					in[1] = out[1] = 1;
					both[1] = 0;
					fill_dp(1);
					answer = Math.min(answer, both[N-1]+2);
				}
			}
			
			System.out.println(answer);

		}
	}

	static void fill_dp(int start) {
		// start부터 N까지 in, out, both를 채우는 함수

		for (int i = start; i < N; i++) {
			// both 채우기, bc:both case
			int bc1 = in[i] + 1; // 안쪽은 점령되어 있는 상태에서, 바깥쪽에서 하나 점령함
			int bc2 = out[i] + 1; // 바깥쪽은 점령되어 있는 상태에서, 안쪽에서 하나 점령함
			int bc3 = in_enemy[i] + out_enemy[i] <= W ? both[i] + 1 : Integer.MAX_VALUE;	// 안쪽+바깥쪽 같이 점령 가능한 상황에서 세로로 점령
			int bc4 = i>0 ? in_enemy[i-1]+in_enemy[i]<=W && out_enemy[i-1]+out_enemy[i]<=W ? both[i-1]+2:Integer.MAX_VALUE : Integer.MAX_VALUE;	//두줄을 가로로 점령
			both[i+1] = Math.min(Math.min(bc1,bc2),Math.min(bc3, bc4));
			if (i < N - 1) {
				// in, out 채우기
				int ic1 = both[i+1]+1;	//한칸만 점령
				int ic2 = in_enemy[i+1]+in_enemy[i]<=W?out[i]+1:Integer.MAX_VALUE; //두칸 점령
				in[i+1] = Math.min(ic1, ic2);
				
				int oc1 = both[i+1]+1;	//한칸만 점령
				int oc2 = out_enemy[i+1]+out_enemy[i]<=W?in[i]+1:Integer.MAX_VALUE; //두칸 점령
				out[i+1] = Math.min(oc1,oc2);
			}
		}
	}
}


