import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int S = sc.nextInt();
		int P = sc.nextInt();
		String data = sc.next();
		int need_A = sc.nextInt();
		int need_C = sc.nextInt();
		int need_G = sc.nextInt();
		int need_T = sc.nextInt();

		int cur_A = 0, cur_C = 0, cur_T = 0, cur_G = 0;
		for(int i = 0 ;i<P;i++) {
			if(data.charAt(i)=='A')cur_A++;
			if(data.charAt(i)=='C')cur_C++;
			if(data.charAt(i)=='T')cur_T++;
			if(data.charAt(i)=='G')cur_G++;
		}
		
		int answer = 0;
		int start = 0;
		int end = P;
		while(true) {
			if(cur_A >= need_A && cur_C >= need_C && cur_T >= need_T && cur_G >= need_G)answer++;
			if(end==S)break;
			if(data.charAt(start)=='A')cur_A--;
			if(data.charAt(start)=='C')cur_C--;
			if(data.charAt(start)=='T')cur_T--;
			if(data.charAt(start)=='G')cur_G--;
			if(data.charAt(end)=='A')cur_A++;
			if(data.charAt(end)=='T')cur_T++;
			if(data.charAt(end)=='C')cur_C++;
			if(data.charAt(end)=='G')cur_G++;
			
			start++;
			end++;
		}
		System.out.println(answer);
	}
}