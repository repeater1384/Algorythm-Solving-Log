import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String input;
		while (true) {
			input = scanner.nextLine();
			if (input.equals("END")) {
				break;
			}
			for (int i = 0; i < input.length(); i++) {
				System.out.print(input.charAt(input.length() - i - 1));
			}
			System.out.println();
		}
	}
}
