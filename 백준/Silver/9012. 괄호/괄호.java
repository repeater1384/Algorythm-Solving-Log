import java.util.*;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while (T-- > 0) {
			int temp = 0;
			String data = sc.next();
			
			for (int j = 0; j < data.length(); j++) {
				if (data.charAt(j) == '(')
					temp++;
				else if (temp-- == 0)
					break;

			}
			System.out.println(temp == 0 ? "YES" : "NO");
		}
		sc.close();
	}
}