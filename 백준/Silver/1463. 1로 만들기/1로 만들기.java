import java.util.Scanner;
 
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		System.out.println(recursive(N,0));
		sc.close();
	}

	static int recursive(int cur, int count){
		if(cur<=1)
			return count;
		return Math.min(recursive(cur/2, count+1+(cur%2)), recursive(cur/3, count+1+(cur%3)));
	}	
}