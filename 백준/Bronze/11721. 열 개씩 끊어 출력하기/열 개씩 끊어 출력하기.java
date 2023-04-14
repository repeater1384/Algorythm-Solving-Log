import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String input = scanner.nextLine();
		int index = 0;
		while (true) {

			try {
				if (index % 10 == 0 && index !=0)
					System.out.println();
				System.out.print(input.charAt(index));
				index++;
			} catch (Exception e) {
				break;
			}

		}
		scanner.close();
	}
}
