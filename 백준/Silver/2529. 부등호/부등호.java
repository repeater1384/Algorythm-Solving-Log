import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N;
	static char[] arr;
	static String maxAnswer;
	static String minAnswer ;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = Integer.parseInt(sc.nextLine());
		String[] temp = sc.nextLine().split(" ");
		arr = new char[N];
		for (int i = 0; i < N; i++)
			arr[i] = temp[i].charAt(0);
		maxAnswer = "0";
		minAnswer = "9999999999999";
		dfs(0, new int[N + 1], new boolean[10]);
		System.out.println(maxAnswer);
		System.out.println(minAnswer);
	}

	static void dfs(int depth, int[] selected, boolean[] visited) {
		if (depth >= 2) {
			if (arr[depth - 2] == '>' && selected[depth - 2] < selected[depth - 1])
				return;
			if (arr[depth - 2] == '<' && selected[depth - 2] > selected[depth - 1])
				return;
		}

		if (depth == N + 1) {
			String result = "";
			for (int i = 0; i <= N; i++) {
				result += selected[i];
			}
			if(maxAnswer.compareTo(result)<0) {
				maxAnswer = result;
			}
			if(minAnswer.compareTo(result)>0) {
				minAnswer = result;
			}
			return;
		}

		for (int i = 0; i <= 9; i++) {
			if (!visited[i]) {
				selected[depth] = i;
				visited[i] = true;
				dfs(depth + 1, selected, visited);
				visited[i] = false;
			}
		}
	}
}