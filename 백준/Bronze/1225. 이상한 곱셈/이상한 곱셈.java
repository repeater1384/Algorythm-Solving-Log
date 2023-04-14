import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String A = sc.next();
		String B = sc.next();
		long answer = 0;
		for(int i = 0 ;i<A.length();i++)
			for(int j = 0 ;j<B.length();j++)
				answer += (long)(A.charAt(i)-'0') * (B.charAt(j)-'0');
		System.out.println(answer);
	}
}