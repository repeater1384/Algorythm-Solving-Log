import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while (T-- > 0) {
			String cmd = sc.next();

			int max_x = 0, max_y = 0, min_x = 0, min_y = 0;
			int cx = 0, cy = 0;

			int[] dx = { 0, 1, 0, -1 };
			int[] dy = { -1, 0, 1, 0 };
			int di = 0;

			for (int i = 0; i < cmd.length(); i++) {
				switch (cmd.charAt(i)) {
				case 'R':
					di = di == 3 ? 0 : di + 1;
					break;
				case 'L':
					di = di == 0 ? 3 : di - 1;
					break;
				case 'F':
					cx += dx[di];
					cy += dy[di];
					break;
				case 'B':
					cx -= dx[di];
					cy -= dy[di];
					break;
				}
				max_x = Math.max(max_x, cx);
				min_x = Math.min(min_x, cx);
				max_y = Math.max(max_y, cy);
				min_y = Math.min(min_y, cy);
			}
			System.out.println((max_x - min_x) * (max_y - min_y));
		}
	}

}