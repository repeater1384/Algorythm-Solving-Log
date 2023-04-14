import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		for (int i = N - 1; i >= 0; i--)
			arr[i] = Integer.parseInt(br.readLine());

		int answer = 1;
		int cur = arr[0];
		for (int i = 1; i < N; i++) {
			if (cur < arr[i]) {
				answer++;
				cur = arr[i];
			}
		}

		System.out.println(answer);
		br.close();

	}

}