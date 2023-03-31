import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] sinMat = new int[N];
		int[] sseunMat = new int[N];
		for(int i = 0 ;i<N;i++) {
			sinMat[i]=sc.nextInt();
			sseunMat[i]=sc.nextInt();
		}
		
		int answer = Integer.MAX_VALUE;
		for(int flag = 1 ; flag<(1<<N);flag++) {
			int sinMul = 1, sseunHap = 0;
			for(int i = 0 ;i<N;i++) {
				if((flag & (1<<i))!=0) {
					sinMul *= sinMat[i];
					sseunHap += sseunMat[i];
				}
			}
			answer = Math.min(answer, Math.abs(sinMul-sseunHap));
		}
		System.out.println(answer);
		sc.close();
	}
}