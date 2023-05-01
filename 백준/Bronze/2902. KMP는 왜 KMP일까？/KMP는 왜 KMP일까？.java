import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String input=scanner.next();
		
		for(int i = 0 ;i<input.length();i++) {
			if(input.charAt(i)>='A' && input.charAt(i)<='Z')
				System.out.print(input.charAt(i));
		}
	}
}
