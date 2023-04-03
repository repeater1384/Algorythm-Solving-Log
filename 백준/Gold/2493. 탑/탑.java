import java.util.*;

public class Main {

	static Stack<Integer> stack;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.nextLine();
		String[] temp = sc.nextLine().split(" ");
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(temp[i]);
		}
		int[] result = new int[N];
		stack = new Stack<>();

		for (int i = N - 1; i >= 0; i--) {
			while (stack.size() > 0 && arr[i] > arr[stack.peek()]) {
				result[stack.peek()] = i + 1;
				stack.pop();
			}
			stack.push(i);
		}

		for (int i = 0; i < N; i++) {
			System.out.print(result[i] + " ");
		}
	}
}