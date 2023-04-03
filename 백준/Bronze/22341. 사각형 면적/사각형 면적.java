import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int C = sc.nextInt();

		int X = N;
		int Y = N;
		while (C-- > 0) {
			int x = sc.nextInt();
			int y = sc.nextInt();

			if (X <= x || Y <= y)
				continue;

			int garo = X * y;
			int sero = x * Y;

			if (garo >= sero)
				Y = y;
			else
				X = x;

		}
		
		System.out.println(X*Y);
	}

}
