import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str_word = sc.nextLine();
		int[] int_arr = new int[str_word.length()];
		
		for(int i = 0 ;i<str_word.length();i++) {
			int_arr[i] = str_word.charAt(i)-3;
			if(int_arr[i]< (int)'A')int_arr[i] += 26;
		}
		
		for(int e:int_arr)System.out.print((char)e);
		System.out.println();
		
	}

}
