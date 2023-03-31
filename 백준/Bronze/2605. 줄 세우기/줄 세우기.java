import java.util.LinkedList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		LinkedList<Integer> array = new LinkedList<>();

		for (int num = 1; num <= N; num++) {
			int order = sc.nextInt();
			array.add(num - order - 1, num);
		}
		for (int num : array)
			System.out.print(num + " ");
	}
}