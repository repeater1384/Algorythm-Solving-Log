import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int x = scanner.nextInt();
		int y = scanner.nextInt();
		int totDay =0;
		String[] week = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
		int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		
		for(int i = 0 ;i<x-1;i++) {
			totDay += daysInMonth[i];
		}
		
		System.out.println(week[(totDay+y)%7]);
        scanner.close();
	}
}
