import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] arr = new int[N];
		for (int i = 0; i < N; i++)
			arr[i] = sc.nextInt();

		int[] result = get_prev_permutation(arr);
		if (result == null)
			System.out.println(-1);
		else {
			for (int i = 0; i < N; i++)
				System.out.print(arr[i] + " ");
		}
		sc.close();

	}

	public static int[] get_prev_permutation(int[] arr) {
		int N = arr.length;
		for (int i = N - 2; i >= 0; i--) {
			if (arr[i] <= arr[i + 1])
				continue;
			int j;
			for (j = N - 1; j >= 0; j--) {
				if (arr[i] > arr[j])
					break;
			}
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;

			i++;
			int K = N - 1;
			while (i < K) {
				temp = arr[i];
				arr[i] = arr[K];
				arr[K] = temp;
				i++;K--;
			}
			return arr;
		}
		return null;
	}
}