import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int len = Integer.parseInt(scanner.nextLine());
		String num = scanner.nextLine();
		int sum = 0;

		for (int i = 0; i < len; i++) {
			sum += Integer.parseInt(num.charAt(i)+"");
		}
		
		System.out.println(sum);
	}
}
