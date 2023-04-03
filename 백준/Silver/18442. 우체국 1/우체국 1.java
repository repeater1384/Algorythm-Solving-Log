import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static long L;
	static long answer1;
	static long[] answer2;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		st = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(st.nextToken());
		int P = Integer.parseInt(st.nextToken());
		L = Long.parseLong(st.nextToken());

		st = new StringTokenizer(br.readLine());
		long[] arr = new long[V];
		for (int i = 0; i < V; i++)
			arr[i] = Long.parseLong(st.nextToken());

		answer1 = Long.MAX_VALUE;
		comb(0, 0, new long[P], arr, P);
		System.out.println(answer1);
		for (long i : answer2) {
			System.out.print(i + " ");
		}
	}

	static void comb(int depth, int start, long[] result, long[] arr, int r) {
		if (depth == r) {
			long cost = 0;
			for (long pos1 : arr) {
				long cur = Long.MAX_VALUE;
				for (long pos2 : result) {
					cur = Math.min(cur, getDis(pos1, pos2));
				}
				cost += cur;
			}
			
			if (cost < answer1) {
				answer1 = cost;
				answer2 = result.clone();
			}
			return;
		}
		for (int i = start; i < arr.length; i++) {
			result[depth] = arr[i];
			comb(depth + 1, i + 1, result, arr, r);
		}
	}

	static long getDis(long a, long b) {
		return Math.min(Math.abs(a - b), L - Math.abs(a - b));
	}

}
