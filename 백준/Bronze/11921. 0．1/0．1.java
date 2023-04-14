import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int M = Integer.parseInt(br.readLine());
		
		int temp = 0;
		for(int i = 0 ;i<100;i++) {
			temp += Integer.parseInt(br.readLine());
		}
		System.out.println(100);
		System.out.println(temp);
	}
}