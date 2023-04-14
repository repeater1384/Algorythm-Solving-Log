import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] arr = new long[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		Arrays.sort(arr);

		int a1 = 0, a2 = 0, a3 = 0;
		long min_diff = Long.MAX_VALUE;
		for (int k = 0; k < n - 2; k++) {
			int i = k + 1, j = n - 1;
			while (i < j) {
				long diff = arr[i] + arr[j] + arr[k];
				long abs_diff = Math.abs(diff);
				
				if (min_diff > abs_diff) {
					min_diff = abs_diff;
					a1 = (int) arr[k];
					a2 = (int) arr[i];
					a3 = (int) arr[j];
				}
				
				if (diff > 0)
					j--;
				else
					i++;

			}
		}

		System.out.printf("%d %d %d\n",a1,a2,a3);
		sc.close();
	}

}