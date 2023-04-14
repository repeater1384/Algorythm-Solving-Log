import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		int[][] matrix = new int[2][7];
		
		while(N-- >0) {
			int s = sc.nextInt();
			int y = sc.nextInt();
			matrix[s][y]++;
		}
		int answer = 0 ;
		for(int i = 0;i<2;i++) {
			for(int j = 0 ;j<=6;j++)
				answer += (matrix[i][j]+K-1) / K;
		}
		System.out.println(answer);
	}
}