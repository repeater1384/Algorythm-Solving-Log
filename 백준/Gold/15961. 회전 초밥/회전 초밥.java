import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int D = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());

		int[] arr = new int[N];

		int[] seusi = new int[D + 1];
		for (int i = 0; i < N; i++)
			arr[i] = Integer.parseInt(br.readLine());

		Set<Integer> set = new HashSet<>();
		for (int i = 0; i < K; i++) {
			seusi[arr[i]]++;
			set.add(arr[i]);
		}
		int answer = 0;
		for (int i = K; i < N + K; i++) {
			int cur = (seusi[C] > 0 ? 0 : 1) + set.size();
			answer = Math.max(cur, answer);
//			System.out.println(Arrays.toString(seusi)+" "+cur);

			int remove = i - K;
			int add = i % N;
			seusi[arr[remove]]--;
			if (seusi[arr[remove]] == 0)
				set.remove(arr[remove]);
			seusi[arr[add]]++;
			if(seusi[arr[add]]==1)
				set.add(arr[add]);
		}
		System.out.println(answer);

	}

}