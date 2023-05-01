import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N;
	static int M;
	static int[][] arr;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		arr = new int[N][M];
		for (int j = 0; j < M; j++) {
			int height = sc.nextInt();
			int idx = N-1;
			while(height-->0) {
				arr[idx--][j] = 1;
			}
		}
		
		int answer = 0;
		for(int i = N-1;i>=0;i--) {
			int start=-1,end=-1;
			for(int j = 0 ;j<M;j++) {
				if(arr[i][j]==1) {
					start=j;
					break;
				}
			}
			for(int j = M-1;j>=0;j--) {
				if(arr[i][j]==1) {
					end = j;
					break;
				}
			}
			if(start==end)break;
			int zeroCnt = 0;
			for(int j = start; j<=end;j++) {
				if(arr[i][j]==0) {
					zeroCnt++;
				}else {
					if(zeroCnt==0)continue;
					answer += zeroCnt;
					zeroCnt = 0;
				}
			}
		}
		System.out.println(answer);
		sc.close();
	}
}