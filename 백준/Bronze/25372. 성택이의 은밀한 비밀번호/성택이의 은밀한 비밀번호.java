import java.util.Scanner;

class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		while (N-- > 0) {
			String word = sc.next();
			if(word.length()>=6 && word.length()<=9)System.out.println("yes");
			else System.out.println("no");
		}
	}
}