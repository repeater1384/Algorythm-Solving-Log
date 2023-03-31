import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int K = sc.nextInt();

		int[][] matrix = new int[N][N];
		for (int i = 0; i < N; i++)
			Arrays.fill(matrix[i], 5);

		List<Integer>[][] treeMatrix = new ArrayList[N][N];
		int[][] addNutrients = new int[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				addNutrients[i][j] = sc.nextInt();
				treeMatrix[i][j] = new ArrayList<Integer>();
			}
		}

		while (M-- > 0) {
			int y = sc.nextInt() - 1;
			int x = sc.nextInt() - 1;
			int age = sc.nextInt();
			treeMatrix[y][x].add(age);
		}

		int[] di = { -1, -1, 0, 1, 1, 1, 0, -1 };
		int[] dj = { 0, 1, 1, 1, 0, -1, -1, -1 };

		while (K-- > 0) {
			// spring + summer
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					List<Integer> cur = treeMatrix[i][j];
					Collections.sort(cur);

					List<Integer> survivedTree = new ArrayList<>();
					boolean isDie = false;
					for (int t = 0; t < cur.size(); t++) {
						if (!isDie && matrix[i][j] >= cur.get(t)) {
							matrix[i][j] -= cur.get(t);
							survivedTree.add(cur.get(t) + 1);
						} else {
							matrix[i][j] += cur.get(t) / 2;
							isDie = true;
						}
					}

					treeMatrix[i][j] = survivedTree;

				}
			}

			// fall + winter
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					List<Integer> cur = treeMatrix[i][j];
					for (int t = 0; t < cur.size(); t++) {
						if (cur.get(t) % 5 == 0) {
							for (int k = 0; k < 8; k++) {
								int ni = i + di[k];
								int nj = j + dj[k];
								if (0 <= ni && ni < N && 0 <= nj && nj < N) {
									treeMatrix[ni][nj].add(1);
								}
							}
						}
					}
					matrix[i][j] += addNutrients[i][j];
				}
			}
		}
		
		int answer = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				answer += treeMatrix[i][j].size();
			}
		}
		System.out.println(answer);
		sc.close();
	}
}