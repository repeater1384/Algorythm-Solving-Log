import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	static int N, M;
	static char[][] matrix;

	public static void main(String[] args) throws IOException {
		// 입력을 위한 코드.
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		matrix = new char[N][M];
		for (int i = 0; i < N; i++)
			matrix[i] = br.readLine().toCharArray();

		for (int y = 0; y < N; y++) {
			for (int x = 0; x < M; x++) {
				// 빈칸이 아니면 블럭을 넣어보지 않는다.
				if (matrix[y][x] != '.')
					continue;

				char canPutBlock = getCanPutBlock(y, x);
				// 기본 null 문자가 아니면 찾은거임.
				if (canPutBlock != '\0') {
					System.out.printf("%d %d %c\n", y + 1, x + 1, canPutBlock);
				}
			}
		}
	}

	static char getCanPutBlock(int y, int x) {
		// + 블럭부터 체크.
		// + 블럭을 놓을수 있으려면 1. 일단 가장자리가 아니여야하고, 2. 모든 블럭과 연결이 되어야함.
		if ((y > 0 && y < N - 1 && x > 0 && x < M - 1)
				&& (matrix[y - 1][x] == '|' || matrix[y - 1][x] == '+' || matrix[y - 1][x] == '1'
						|| matrix[y - 1][x] == '4')
				&& (matrix[y + 1][x] == '|' || matrix[y + 1][x] == '+' || matrix[y + 1][x] == '2'
						|| matrix[y + 1][x] == '3')
				&& (matrix[y][x - 1] == '-' || matrix[y][x - 1] == '+' || matrix[y][x - 1] == '1'
						|| matrix[y][x - 1] == '2')
				&& (matrix[y][x + 1] == '-' || matrix[y][x + 1] == '+' || matrix[y][x + 1] == '3'
						|| matrix[y][x + 1] == '4')) {
			return '+';
		}
		for (char curBlock : new char[] { '|', '-', '1', '2', '3', '4' }) {
			// +블럭을 제외한 나머지 6개 블럭 놓아보기.
			// 각 블럭들은 존재할수 있는 조건들이 있음. continue로 하나하나 건너뛰어가면서 해결.
			if (curBlock == '|' || curBlock == '2' || curBlock == '3') {
				if (y == 0 || !(matrix[y - 1][x] == '|' || matrix[y - 1][x] == '+' || matrix[y - 1][x] == '1'
						|| matrix[y - 1][x] == '4'))
					continue;
			}
			if (curBlock == '|' || curBlock == '1' || curBlock == '4') {
				if (y == N - 1 || !(matrix[y + 1][x] == '|' || matrix[y + 1][x] == '+' || matrix[y + 1][x] == '2'
						|| matrix[y + 1][x] == '3'))
					continue;
			}
			if (curBlock == '-' || curBlock == '3' || curBlock == '4') {
				if (x == 0 || !(matrix[y][x - 1] == '-' || matrix[y][x - 1] == '+' || matrix[y][x - 1] == '1'
						|| matrix[y][x - 1] == '2'))
					continue;
			}
			if (curBlock == '-' || curBlock == '1' || curBlock == '2') {
				if (x == M - 1 || !(matrix[y][x + 1] == '-' || matrix[y][x + 1] == '+' || matrix[y][x + 1] == '3'
						|| matrix[y][x + 1] == '4'))
					continue;
			}
			return curBlock;
		}
		return '\0';

	}
}