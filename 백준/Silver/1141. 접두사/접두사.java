import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = Integer.parseInt(sc.nextLine());
		String[] arr = new String[N];
		for (int i = 0; i < N; i++)
			arr[i] = sc.nextLine();

		Set<String> set = new HashSet<>();
		for (int i = 0; i < N; i++) {
			boolean iAmYourFather = false;
			for (int j = 0; j < N; j++) {
				if (i == j || arr[i].equals(arr[j]))
					continue;
				if (arr[j].startsWith(arr[i])) {
					iAmYourFather = true;
					break;
				}
			}
			if (!iAmYourFather)
				set.add(arr[i]);
		}
		System.out.println(set.size());
		sc.close();
	}
}