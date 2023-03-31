import java.util.Scanner;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		char[] arr = new char[36];
		ArrayList<Character> answer = new ArrayList<>();

		for (int i = 0; i < 36; i++) {
			if (i < 10)
				arr[i] = (char) (i + '0');
			else
				arr[i] = (char) (55 + i);
		}

		while (A > 0) {
			answer.add(arr[A % B]);
			A /= B;
		}

		for (int i = answer.size() - 1; i >= 0; i--) {
			System.out.print(answer.get(i));
		}
	}
}
