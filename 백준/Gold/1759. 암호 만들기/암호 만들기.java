import java.util.*;

public class Main {
	static char[] letter;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int L = sc.nextInt(), C = sc.nextInt();
		sc.nextLine();

		letter = sc.nextLine().replace(" ", "").toCharArray();
		Arrays.sort(letter);

		char[] pw = new char[L];
		genPW(pw, 0, 0);
	}

	static void genPW(char[] password, int depth, int start) {
		if (depth == password.length) {
			int mo = 0, ja = 0;
			for (char p : password)
				if (p == 'a' || p == 'e' || p == 'i' || p == 'o' || p == 'u')
					mo++;
				else
					ja++;
			if (mo >= 1 && ja >= 2)
				System.out.println(new String(password));
			return;
		}
		for (int k = start; k < letter.length; k++) {
			password[depth] = letter[k];
			genPW(password, depth + 1, k + 1);
		}
	}
}