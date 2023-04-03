import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

class Shark {
	int r;
	int c;
	int dir;
	int[][] priority;

	public Shark(int r, int c) {
		super();
		this.r = r;
		this.c = c;
	}

	@Override
	public String toString() {
		return "Shark [r=" + r + ", c=" + c + ", dir=" + dir + ", priority=" + Arrays.deepToString(priority) + "]";
	}

}

class Smell {
	int sharkNum, leftYear;

	public Smell(int sharkNum, int leftYear) {
		super();
		this.sharkNum = sharkNum;
		this.leftYear = leftYear;
	}
}

public class Main {
	static int N, M, K;
	static int[][] mainMatrix;
	static Shark[] sharkArr;
	static Smell[][] smellMatrix;

	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { -1, 1, 0, 0 };

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());// 상어의 수
		K = Integer.parseInt(st.nextToken()); // 냄새가 사라지는 시간

		mainMatrix = new int[N][N];
		smellMatrix = new Smell[N][N];
		sharkArr = new Shark[M + 1];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				mainMatrix[i][j] = Integer.parseInt(st.nextToken());
				if (mainMatrix[i][j] > 0) {
					sharkArr[mainMatrix[i][j]] = new Shark(i, j);
					smellMatrix[i][j] = new Smell(mainMatrix[i][j], K);
				}
			}
		}

		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= M; i++) {
			sharkArr[i].dir = Integer.parseInt(st.nextToken()) - 1;
		}

		for (int i = 1; i <= M; i++) {
			int[][] temp = new int[4][4];
			for (int x = 0; x < 4; x++) {
				st = new StringTokenizer(br.readLine());
				for (int y = 0; y < 4; y++) {
					temp[x][y] = Integer.parseInt(st.nextToken()) - 1;
				}
			}
			sharkArr[i].priority = temp;
		}

		int answer = -1;
		int leftShark = M;
		int year = 0;
		while (year <= 1000) {
			if (leftShark == 1) {
				answer = year;
				break;
			}
			year++;
			Smell[][] tempSmellMatrix = new Smell[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (smellMatrix[i][j] == null)
						continue;
					Smell curSmell = smellMatrix[i][j];
					if (curSmell.leftYear > 1)
						tempSmellMatrix[i][j] = new Smell(curSmell.sharkNum, curSmell.leftYear - 1);
				}
			}
			// 상어의 이동 + 냄새 뿌리기
			for (int sharkIdx = 1; sharkIdx <= M; sharkIdx++) {
				if (sharkArr[sharkIdx] == null)
					continue;
				Shark curShark = sharkArr[sharkIdx];
				int r = curShark.r;
				int c = curShark.c;
				int dir = curShark.dir;
				int[] nextDir = curShark.priority[dir];

				List<int[]> emptyPlace = new ArrayList<>();
				List<int[]> mySmellPlace = new ArrayList<>();

				for (int k : nextDir) {
					int nr = r + dy[k];
					int nc = c + dx[k];
					if (0 <= nr && nr < N && 0 <= nc && nc < N) {
						if (smellMatrix[nr][nc] == null) {
							emptyPlace.add(new int[] { nr, nc, k });
						} else if (smellMatrix[nr][nc].sharkNum == sharkIdx) {
							mySmellPlace.add(new int[] { nr, nc, k });
						}
					}
				}

				if (emptyPlace.size() > 0) {
					int[] nextPlace = emptyPlace.get(0);
					int nr = nextPlace[0];
					int nc = nextPlace[1];
					int nd = nextPlace[2];
					if (mainMatrix[nr][nc] == 0) {
						mainMatrix[r][c] = 0;
						mainMatrix[nr][nc] = sharkIdx;
						curShark.r = nr;
						curShark.c = nc;
						curShark.dir = nd;
						tempSmellMatrix[nr][nc] = new Smell(sharkIdx,K); 
					} else {
						leftShark--;
						if (sharkIdx > mainMatrix[nr][nc]) {
							mainMatrix[r][c] = 0;
							sharkArr[sharkIdx] = null;
							continue;
						}
					}
				} else {
					int[] nextPlace = mySmellPlace.get(0);
					int nr = nextPlace[0];
					int nc = nextPlace[1];
					int nd = nextPlace[2];
					mainMatrix[r][c] = 0;
					mainMatrix[nr][nc] = sharkIdx;
					curShark.r = nr;
					curShark.c = nc;
					curShark.dir = nd;
					tempSmellMatrix[nr][nc] = new Smell(sharkIdx,K); 
				}
			}
			smellMatrix = tempSmellMatrix;
//			for (int[] row : mainMatrix) {
//				System.out.println(Arrays.toString(row));
//			}
//			System.out.println("-----------------");
		}
		System.out.println(answer);
//		for (Shark s : sharkArr) {
//			System.out.println(s);
//		}
		sc.close();
	}
}