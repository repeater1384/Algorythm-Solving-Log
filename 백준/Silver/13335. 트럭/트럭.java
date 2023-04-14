import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
//		File file = new File("input.txt");
//		try {
//			BufferedWriter bw = new BufferedWriter(new FileWriter(file));
//			bw.write("1000 100 10\n");
//			for(int i = 0 ;i<1000;i++)
//				bw.write("10 ");
//			bw.close();
//		} catch (IOException e) {
//		}
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int W = sc.nextInt();
		int L = sc.nextInt();
		int[] arr = new int[N + 1];
		for (int i = 0; i < N; i++)
			arr[i] = sc.nextInt();

		LinkedList<Integer> onBridge = new LinkedList<>();
		for (int i = 0; i < W - 1; i++)
			onBridge.add(0);
		onBridge.add(arr[0]);
		int onBridgeSum = arr[0];
		int answer = 1;
		int idx = 1;
		while (idx < N) {
			int out = onBridge.poll();
			onBridgeSum -= out;
			if (onBridgeSum + arr[idx] <= L) {
				onBridge.add(arr[idx]);
				onBridgeSum += arr[idx++];
			} else {
				onBridge.add(0);
			}
			answer++;
		}
		while (onBridgeSum > 0) {
			answer++;
			int out = onBridge.poll();
			onBridgeSum -= out;
		}
		System.out.println(answer);
		sc.close();
	}
}