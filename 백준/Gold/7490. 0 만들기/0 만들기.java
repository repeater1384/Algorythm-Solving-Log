import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
	static List<String> answer;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int t = 0; t < T; t++) {
			int N = sc.nextInt();
			answer = new ArrayList<>();
			dfs(new String[N - 1], 0, N);
			Collections.sort(answer);
			for (String a : answer) {
				System.out.println(a);
			}
			System.out.println();
		}
		sc.close();
	}

	static void dfs(String[] result, int depth, int N) {
		if (depth == N - 1) {
			String temp = "1";
			for (int i = 0; i < N - 1; i++) {
				temp += result[i] + (i + 2);
			}
			char[] cur = temp.toCharArray();
			int idx = 0;
			for (int i = 0; i < cur.length; i++) {
				if ('1' <= cur[i] && cur[i] <= '9' || cur[i] == ' ')
					continue;
				idx = i;
				break;
			}
			if (idx == 0)
				return;

			int calc = 0;
			for (int i = 0; i < idx; i++) {
				if (cur[i] == ' ')
					continue;
				calc *= 10;
				calc += cur[i] - '0';
			}
			int num = 0;
			char op = cur[idx];

			for (int i = idx + 1; i < cur.length; i++) {
				if (cur[i] == ' ')
					continue;
				if ('1' <= cur[i] && cur[i] <= '9') {
					num *= 10;
					num += cur[i] - '0';
				} else {
					if (op == '+') {
						calc += num;
					}
					if (op == '-') {
						calc -= num;
					}
					op = cur[i];
					num = 0;
				}
			}
			if (op == '+') {
				calc += num;
			}
			if (op == '-') {
				calc -= num;
			}

			if (calc == 0) {
				answer.add(temp);
			}
			return;
		}
		result[depth] = "+";
		dfs(result, depth + 1, N);
		result[depth] = "-";
		dfs(result, depth + 1, N);
		result[depth] = " ";
		dfs(result, depth + 1, N);
	}
}