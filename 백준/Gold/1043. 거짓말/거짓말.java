import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Main {
	static int[] parents;
	static boolean[] know_truth;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		parents = new int[N + 1];
		for (int i = 1; i <= N; i++)
			parents[i] = i;

		know_truth = new boolean[N + 1];
		int truth_n = sc.nextInt();

		for (int i = 0; i < truth_n; i++) {
			know_truth[sc.nextInt()] = true;
		}

		ArrayList<int[]> parties = new ArrayList<>();
		for (int i = 0; i < M; i++) {
			int party_n = sc.nextInt();
			int[] party = new int[party_n];
			for (int j = 0; j < party_n; j++)
				party[j] = sc.nextInt();
			parties.add(party);
		}
		for (int[] party : parties) {
			for (int i = 0; i < party.length - 1; i++) {
				for (int j = i + 1; j < party.length; j++) {
					union(party[i], party[j]);
				}
			}
		}

		for (int i = 1; i <= N; i++) {
			if (know_truth[find(i)])
				know_truth[i] = true;
		}

		int answer = 0;
		for (int[] party : parties) {
			boolean check = true;
			for (int member : party) {
				if (know_truth[member]) {
					check = false;
					break;
				}
			}
			if (check)
				answer++;
		}
		System.out.println(answer);
	}

	static int find(int x) {
		if (x == parents[x])
			return x;
		return parents[x] = find(parents[x]);
	}

	static void union(int x, int y) {
		x = find(x);
		y = find(y);

		if (know_truth[x] || know_truth[y]) {
			know_truth[x] = true;
			know_truth[y] = true;
		}
		if (x > y) {
			parents[x] = y;
		} else {
			parents[y] = x;
		}
	}
}