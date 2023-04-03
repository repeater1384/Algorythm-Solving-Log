import java.util.Scanner;

public class Main {
	static int MAX_DEPTH;
	static StringBuilder sb;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		MAX_DEPTH = sc.nextInt();
		sb = new StringBuilder();
		sol(0);
		System.out.println(sb.toString());
		sc.close();
	}

	static void sol(int depth) {
		if (depth > MAX_DEPTH)
			return;
		if (depth == 0)
			sb.append("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.").append('\n');

		String head = new String(new char[depth]).replace("\0", "____");

		sb.append(head).append("\"재귀함수가 뭔가요?\"").append('\n');
		if (depth == MAX_DEPTH)
			sb.append(head).append("\"재귀함수는 자기 자신을 호출하는 함수라네\"").append('\n');
		else {
			sb.append(head).append("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.").append('\n');
			sb.append(head).append("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.").append('\n');
			sb.append(head).append("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"").append('\n');
			sol(depth + 1);
		}
		sb.append(head).append("라고 답변하였지.").append('\n');
	}
}