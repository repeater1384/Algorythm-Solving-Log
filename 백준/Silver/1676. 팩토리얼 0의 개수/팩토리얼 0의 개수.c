#include<stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int result = 0;
	for (int i = 5; i <= n; i *= 5)
		result += n / i;
	printf("%d\n", result);

	return 0;
}