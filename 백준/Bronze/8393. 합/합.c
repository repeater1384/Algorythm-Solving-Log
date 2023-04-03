#include <stdio.h>

int main() {
	int a;
	int answer = 0;

	scanf("%d", &a);

	for (int i = 1; i <= a; i++) {
		answer += i;
	}

	printf("%d", answer);
}