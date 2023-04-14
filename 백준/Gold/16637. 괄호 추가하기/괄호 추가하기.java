import java.util.Scanner;

public class Main {

	static int answer = Integer.MIN_VALUE;
	static int N;
	static String cmd;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = Integer.parseInt(sc.nextLine());
		cmd = "+" + sc.nextLine();
		dfs(0,1);
		System.out.println(answer);
		sc.close();
	}
	
	static void dfs(int cur, int idx) {
		if(idx>=N+1) {
			answer = Math.max(cur, answer);
			return;
		}
		
		char op = cmd.charAt(idx-1);
		int a = cur;
		int b = cmd.charAt(idx)-'0';
		dfs(calc(a,b,op),idx+2);
		if(idx<N-1) {
			int c = cmd.charAt(idx+2)-'0';
			char op2 = cmd.charAt(idx+1);
			int temp = calc(b,c,op2);
			dfs(calc(cur,temp,op),idx+4);
		}
	}
	
	static int calc(int a, int b, char op) {
		switch(op) {
		case '+':return a+b;
		case '-':return a-b;
		case '*':return a*b;
		}
		return -1;
	}
}