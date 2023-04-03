import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] stack = new int[10000];
		int top = 0;

		StringBuilder sb = new StringBuilder();
		while (N-- > 0) {
			String cmd = br.readLine();
			if (cmd.startsWith("push")) {
				stack[top++] = Integer.parseInt(cmd.substring(5));
			} else if (cmd.equals("pop")) {
				if (top == 0) {
					sb.append(-1).append('\n');
				} else {
					sb.append(stack[--top]).append('\n');
					stack[top] = 0;
				}
			} else if (cmd.equals("size")) {
				sb.append(top).append('\n');
			} else if (cmd.equals("empty")) {
				sb.append(top == 0 ? 1 : 0).append('\n');
			} else if (cmd.equals("top")) {
				if (top == 0) {
					sb.append(-1).append('\n');
				} else {
					sb.append(stack[top - 1]).append('\n');
				}
			}
		}

		System.out.println(sb.toString());

	}

}