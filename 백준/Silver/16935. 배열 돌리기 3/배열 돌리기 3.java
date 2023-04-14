import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());

		arr = new int[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++)
				arr[i][j] = Integer.parseInt(st.nextToken());
		}

		st = new StringTokenizer(br.readLine());
		while (R-- > 0) {
			command(Integer.parseInt(st.nextToken()));
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[0].length; j++)
				sb.append(arr[i][j]).append(' ');
			sb.append('\n');
		}
		System.out.println(sb.toString());
		br.close();
	}

	static void command(int cmd) {
		int N = arr.length;
		int M = arr[0].length;
		int[][] result;
		int[][] temp;
		switch (cmd) {
		case 1:
			result = new int[N][M];
			for (int i = 0; i < N; i++)
				for (int j = 0; j < M; j++)
					result[i][j] = arr[N - i - 1][j];
			arr = result;
			break;
		case 2:
			result = new int[N][M];
			for (int i = 0; i < N; i++)
				for (int j = 0; j < M; j++)
					result[i][j] = arr[i][M - j - 1];
			arr = result;
			break;
		case 3:
			result = new int[M][N];
			for (int i = 0; i < N; i++)
				for (int j = 0; j < M; j++)
					result[j][N - i - 1] = arr[i][j];
			arr = result;
			break;
		case 4:
			result = new int[M][N];
			for (int i = 0; i < N; i++)
				for (int j = 0; j < M; j++)
					result[M - j - 1][i] = arr[i][j];
			arr = result;
			break;
		case 5:
			result = new int[N][M];
			temp = new int[N / 2][M / 2];
			for (int i = 0; i < N / 2; i++)
				for (int j = 0; j < M / 2; j++)
					temp[i][j] = arr[i][j];

			for (int i = 0; i < N / 2; i++)
				for (int j = 0; j < M / 2; j++)
					result[i][j] = arr[i + N / 2][j];

			for (int i = 0; i < N / 2; i++)
				for (int j = 0; j < M / 2; j++)
					result[i + N / 2][j] = arr[i + N / 2][j + M / 2];

			for (int i = 0; i < N / 2; i++)
				for (int j = 0; j < M / 2; j++)
					result[i + N / 2][j + M / 2] = arr[i][j + M / 2];

			for (int i = 0; i < N / 2; i++)
				for (int j = 0; j < M / 2; j++)
					result[i][j + M / 2] = temp[i][j];
			arr = result;
			break;
		case 6:
			result = new int[N][M];
			temp = new int[N / 2][M / 2];
			for (int i = 0; i < N / 2; i++)
				for (int j = 0; j < M / 2; j++)
					temp[i][j] = arr[i][j];

			for (int i = 0; i < N / 2; i++)
				for (int j = 0; j < M / 2; j++)
					result[i][j] = arr[i][j + M / 2];

			for (int i = 0; i < N / 2; i++)
				for (int j = 0; j < M / 2; j++)
					result[i][j + M / 2] = arr[i + N / 2][j + M / 2];

			for (int i = 0; i < N / 2; i++)
				for (int j = 0; j < M / 2; j++)
					result[i + N / 2][j + M / 2] = arr[i + N / 2][j];

			for (int i = 0; i < N / 2; i++)
				for (int j = 0; j < M / 2; j++)
					result[i + N / 2][j] = temp[i][j];
			arr = result;
			break;
		}
	}

}