import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int M = scanner.nextInt();
		scanner.close();
		int total = 0, min=0;
		
		for(int i =M ; i>=N;i--) {
			if(checkPrime(i)) {
				total += i;
				min = i;
			}
		}
		if(min != 0) {
		System.out.println(total);
		System.out.println(min);
		}
		else
			System.out.println(-1);

	}

	static boolean checkPrime(int n) {
		if(n==2)
			return true;
		if(n<=1)
			return false;
		for (int i = 2; i < Math.sqrt(n) + 1; i++)
			if (n % i == 0)
				return false;
		
		return true;
	}
}
