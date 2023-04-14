import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] sortedArr = new int[N];
		int[] origArr = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < N; i++) {
			origArr[i] = sortedArr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(sortedArr);

		Map<Integer, Integer> map = new HashMap<>();
		int rank = 0;
		map.put(sortedArr[0], rank);
		for (int i = 1; i < N; i++) {
			if (sortedArr[i] != sortedArr[i - 1])
				map.put(sortedArr[i], ++rank);
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			sb.append(map.get(origArr[i])).append(' ');
		}

		System.out.println(sb.toString());
	}

}