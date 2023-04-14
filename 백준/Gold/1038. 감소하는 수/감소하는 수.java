import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		List<Long> decreaseNum = new ArrayList<>();
		for(int flag = 1 ; flag<(1<<10);flag++) {
			long cur = 0;
			for(int i = 0 ;i<10;i++) {
				if((flag & (1<<i))!=0) {
					cur += (9-i);
					cur *= 10;
				}
			}
			decreaseNum.add(cur/10);
		}
		Collections.sort(decreaseNum);
		try {
			System.out.println(decreaseNum.get(N));
		}catch (Exception e) {
			System.out.println(-1);
		}
		sc.close();
	}
}