import java.util.Arrays;
import java.util.Scanner;

class Heap {

	int MAX_SIZE;
	int size = 0;
	long[] data;

	public Heap(int mAX_SIZE) {
		super();
		MAX_SIZE = mAX_SIZE;
		data = new long[MAX_SIZE + 1];
	}

	void add(long l) {
		data[++size] = l;
		int idx = size;
		while (idx > 1) {
			long parent = data[idx / 2];
			if (parent <= data[idx])
				break;
			data[idx / 2] = data[idx];
			data[idx] = parent;
			idx /= 2;
		}
	}

	long pop() {
		if (size == 0)
			return -1;
		long returnValue = data[1];

		data[1] = data[size];
		data[size--] = 0;
		int idx = 1;
		while (idx * 2 <= size) {
			long cur = data[idx];
			int nextIdx = idx * 2;
			long next = data[nextIdx];
			if (idx * 2 + 1 <= size && next > data[idx * 2 + 1]) {
				nextIdx = idx * 2 + 1;
				next = data[nextIdx];
			}
			
			if (cur < next)
				break;
			
			data[idx] = next;
			data[nextIdx] = cur;
			idx = nextIdx;
		}
		return returnValue;
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();
		Heap pq = new Heap(N);

		while (N-- > 0) {
			pq.add(sc.nextInt());
		}

		while (M-- > 0) {
			long a = pq.pop();
			long b = pq.pop();
			pq.add(a + b);
			pq.add(a + b);
		}
		long answer = 0;
		for (int i = 0; i < pq.data.length; i++) {
			answer += pq.data[i];
		}
		System.out.println(answer);
		sc.close();
	}
}
