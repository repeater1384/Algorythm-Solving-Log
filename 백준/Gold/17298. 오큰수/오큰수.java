import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		int[] answer = new int[N];
		Arrays.fill(answer, -1);

		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < N; i++)
			arr[i] = Integer.parseInt(st.nextToken());

		Stack<Integer> stack = new Stack<>();
		for (int i = 0; i < N; i++) {
			while (stack.size() > 0 && arr[stack.peek()] < arr[i])
				answer[stack.pop()] = arr[i];

			stack.add(i);
		}
		StringBuilder sb = new StringBuilder();
		for (int i : answer)
			sb.append(i).append(' ');
		
		System.out.println(sb.toString());
	}

}