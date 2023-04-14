import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int N;
	static int[][] arr;
	static List<int[]> blackPos;
	static List<int[]> whitePos;
	static int blackAnswer = 0;
	static int whiteAnswer = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		arr = new int[N][N];
		blackPos = new ArrayList<>();
		whitePos = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (sc.nextInt() == 1) {
					if ((i + j) % 2 == 0)
						blackPos.add(new int[] { i, j });
					else
						whitePos.add(new int[] { i, j });
				}
			}
		}

		blackDfs(0, 0);
		whiteDfs(0, 0);
		
		System.out.println(blackAnswer + whiteAnswer);
		sc.close();
	}

	static void blackDfs(int cnt, int idx) {

		if (idx == blackPos.size()) {
			blackAnswer = Math.max(cnt, blackAnswer);
			return;
		}

		int[] cur = blackPos.get(idx);
		int i = cur[0];
		int j = cur[1];

		if (check(i, j)) {
			arr[i][j] = 1;
			blackDfs(cnt + 1, idx + 1);
		}
		arr[i][j] = 0;
		blackDfs(cnt, idx + 1);

	}

	static void whiteDfs(int cnt, int idx) {

		if (idx == whitePos.size()) {
			whiteAnswer = Math.max(cnt, whiteAnswer);
			return;
		}

		int[] cur = whitePos.get(idx);
		int i = cur[0];
		int j = cur[1];

		if (check(i, j)) {
			arr[i][j] = 1;
			whiteDfs(cnt + 1, idx + 1);
		}

		arr[i][j] = 0;
		whiteDfs(cnt, idx + 1);

	}

	static boolean check(int i, int j) {
		for (int d = -N; d < N; d++) {
			if (d == 0 || i + d < 0 || i + d >= N || j + d < 0 || j + d >= N)
				continue;
			if (arr[i + d][j + d] == 1)
				return false;

		}
		for (int d = -N; d < N; d++) {
			if (d == 0 || i + d < 0 || i + d >= N || j - d < 0 || j - d >= N)
				continue;
			if (arr[i + d][j - d] == 1)
				return false;
		}
		return true;
	}
}