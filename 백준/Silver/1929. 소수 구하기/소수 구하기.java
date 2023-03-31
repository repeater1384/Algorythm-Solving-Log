import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int M = scanner.nextInt();
		int N = scanner.nextInt();
		scanner.close();
		
		for(int i = M;i<=N;i++)
			if(checkPrime(i))
				System.out.println(i);
		
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
