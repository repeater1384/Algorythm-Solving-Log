import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int M = sc.nextInt();
		int ball = 1;
		while(M-- > 0) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			if (a == ball)ball = b;
			else if(b == ball)ball = a;
		}
		
		System.out.println(ball);
	}
}
