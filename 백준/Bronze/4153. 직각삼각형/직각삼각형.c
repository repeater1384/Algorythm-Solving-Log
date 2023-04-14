#include <stdio.h>

void swap(int* a, int* b);

int main() {
	int a, b, c;

	while (1) {
		scanf("%d %d %d", &a, &b, &c);
		if (a == 0 && b == 0 && c == 0) {
			break;
		}


		if (a > c) {
			swap(&a, &c);
		}
		if (b > c) {
			swap(&b, &c);
		}
		if (a * a + b * b == c * c) {
			printf("right\n");
		}
		else {
			printf("wrong\n");
		}

	}
	return 0;
}

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}