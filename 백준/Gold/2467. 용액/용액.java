import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		Arrays.sort(arr);

		int i = 0, j = n - 1;
		int a1 = 0, a2 = 0;
		int min_diff = Integer.MAX_VALUE;
		while (i < j) {
			int diff = arr[i] + arr[j];
			int abs_diff = Math.abs(diff);
			if (min_diff >= abs_diff) {
				min_diff = abs_diff;
				a1 = arr[i];
				a2 = arr[j];
			}
			
			if (diff > 0) {
				j--;
			} else {
				i++;
			}
		}

		System.out.println(a1 + " " + a2);
		sc.close();
	}

}