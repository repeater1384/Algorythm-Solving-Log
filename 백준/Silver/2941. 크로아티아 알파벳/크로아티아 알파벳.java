import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine().trim();
		int answer = input.length();
		for (int i = 0; i < input.length(); i++) {
			switch (input.charAt(i)) {
			case 'c':
				if (i < input.length() - 1) {
					if (input.charAt(i + 1) == '=' || input.charAt(i + 1) == '-')
						answer--;
				}
				break;
			case 'd':
				if (i < input.length() - 2) {
					if (input.charAt(i + 1) == 'z' && input.charAt(i + 2) == '=')
						answer--;
				}
				if (i < input.length() - 1) {
					if (input.charAt(i + 1) == '-')
						answer--;
				}
				break;
			case 'l':
				if (i < input.length() - 1) {
					if (input.charAt(i + 1) == 'j')
						answer--;
				}
				break;
			case 'n':
				if (i < input.length() - 1) {
					if (input.charAt(i + 1) == 'j')
						answer--;
				}
				break;
			case 's':
				if (i < input.length() - 1) {
					if (input.charAt(i + 1) == '=')
						answer--;
				}
				break;
			case 'z':
				if (i < input.length() - 1) {
					if (input.charAt(i + 1) == '=')
						answer--;
				}
				break;

			}

		}
		System.out.println(answer);
	}
}
