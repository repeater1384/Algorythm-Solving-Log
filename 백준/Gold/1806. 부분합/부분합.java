import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		int[] arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++)
			arr[i] = Integer.parseInt(st.nextToken());

		int end = 0;
		int sum = 0;
		int answer = Integer.MAX_VALUE;
		
		for (int start = 0; start < N; start++) {
			while (end < N && sum < S) 
				sum += arr[end++];
			
			if(sum>=S)
				answer = Math.min(answer, end - start);
			sum -= arr[start];
		}
		System.out.println(answer == Integer.MAX_VALUE ? 0 : answer);
	}

}