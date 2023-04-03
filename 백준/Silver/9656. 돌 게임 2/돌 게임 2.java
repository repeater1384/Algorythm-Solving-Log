import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int N = (new Scanner(System.in)).nextInt();

		String answer = null;
		if ((N - 1) % 4 == 1 || (N - 1) % 4 == 3)
			answer = "SK";
		else
			answer = "CY";
		System.out.println(answer);
	}

}
