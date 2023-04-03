import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

class Heap3<E> {
	E[] data;
	int size;
	int MAX_SIZE;
	Comparator<E> comp;

	public Heap3(Comparator<E> comp, int MAX_SIZE) {
		this.comp = comp;
		this.MAX_SIZE = MAX_SIZE;
		this.data = (E[]) new Object[this.MAX_SIZE + 1];
		this.size = 0;
	}

	void add(E val) {
		data[++size] = val;
		int idx = size;
		while (idx > 1) {
			E parent = data[idx / 2];
			E cur = data[idx];
			if (comp.compare(parent, cur) < 0) {
				break;
			}
			data[idx / 2] = cur;
			data[idx] = parent;
			idx /= 2;
		}
	}

	E pop() {
		if (size == 0)
			return null;
		E returnVal = data[1];
		data[1] = data[size--];

		int idx = 1;
		while (idx * 2 <= size) {
			E cur = data[idx];
			E child = data[idx * 2];
			int nextIdx = idx * 2;
			if (idx * 2 + 1 <= size && comp.compare(child, data[idx * 2 + 1]) > 0) {
				child = data[idx * 2 + 1];
				nextIdx = idx * 2 + 1;
			}

			if (comp.compare(cur, child) < 0)
				break;

			data[idx] = child;
			data[nextIdx] = cur;
			idx = nextIdx;
		}

		return returnVal;
	}

	E peek() {
		return data[1];
	}

	boolean isEmpty() {
		return size == 0;
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int K = sc.nextInt();
		int N = sc.nextInt();

		Long[] arr = new Long[K];
		PriorityQueue<Long> heap = new PriorityQueue<>();
		for (int i = 0; i < K; i++) {
			arr[i] = (long) sc.nextInt();
			heap.add(arr[i]);
		}
		for (int i = 0; i < N - 1; i++) {
			long cur = heap.poll();
			for (long p : arr) {
				long next = cur * p;
				heap.add(next);
				if (cur % p == 0)
					break;
			}
		}
		System.out.println(heap.poll());
	}
}