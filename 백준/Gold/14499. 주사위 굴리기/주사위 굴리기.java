import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		/*
		 * 				a1
		 *			a5	a2  a6
		 * 				a3
		 * 				a4
		 * 
		 * a2가 바닥. a4가 윗면.
		 * 남쪽으로 굴리면 a1 -> a4 / a2 -> a1 / a3 -> a2 / a4 -> a3
		 * 북쪽으로 굴리면 a1 -> a2 / a2 -> a3 / a3 -> a4 / a4 -> a1
		 * 동쪽으로 굴리면 a2 -> a5 / a5 -> a4 / a4 -> a6 / a6 -> a2
		 * 서쪽으로 굴리면 a2 -> a6 / a6 -> a4 / a4 -> a5 / a5 -> a2
		 */
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		int y = sc.nextInt();
		int x = sc.nextInt();

		int a1 = 0, a2 = 0, a3 = 0, a4 = 0, a5 = 0, a6 = 0;

		int K = sc.nextInt();
		int[][] arr = new int[N][M];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				arr[i][j] = sc.nextInt();

		for (int i = 0; i < K; i++) {
			int cmd = sc.nextInt();
			//동쪽
			if(cmd==1) {
				if(x+1==M)continue;
				int temp = a5;
				x++;
				a5 = a2;
				a2 = a6;
				a6 = a4;
				a4 = temp;
				
			}
			
			if(cmd==2) {
				if(x-1==-1)continue;
				int temp = a6;
				x--;
				a6 = a2;
				a2 = a5;
				a5 = a4;
				a4 = temp;
				
			}
			if(cmd==3) {
				if(y-1==-1)continue;
				int temp = a2;
				y--;
				a2 = a3;
				a3 = a4;
				a4 = a1;
				a1 = temp;
				
			}
			if(cmd==4) {
				if(y+1==N)continue;
				int temp = a2;
				y++;
				a2 = a1;
				a1 = a4;
				a4 = a3;
				a3 = temp;
				
			}
			
			if(arr[y][x]==0)arr[y][x] = a2;
			else {
				a2 = arr[y][x];
				arr[y][x] = 0;
			}
			System.out.println(a4);
			
		}
		sc.close();
	}
}