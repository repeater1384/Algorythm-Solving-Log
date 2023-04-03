import java.util.*;

public class Main {

	public static void main(String[] args) {
		String target = "CAMBRIDGE";
		Scanner sc = new Scanner(System.in);

		String input = sc.nextLine();
		ArrayList<Character> answer = new ArrayList<>();

		for (int i = 0; i < input.length(); i++) {
			boolean find = false;
			for (int j = 0; j < target.length(); j++) {
				if (input.charAt(i) != target.charAt(j)) {
					continue;
				}
				find = true;
			}
			if (!find)
				answer.add(input.charAt(i));
		}

		for (char c : answer) {
			System.out.print(c);
		}
		sc.close();
	}

}
