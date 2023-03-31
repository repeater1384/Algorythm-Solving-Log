#include<stdio.h>


int main() {
	int x, y, N, result;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%d %d", &x, &y);
		for (long long n = 1; ; n++) {
			if (n*n - n + 1 <= y - x && y - x <= n * n) {
				result = n * 2 - 1;
				break;
			}
			else if (n*n < y - x && y - x <= n * n + n) {
				result = n * 2;
				break;
			}
		}
		printf("%d\n", result);
	}
	return 0;
}