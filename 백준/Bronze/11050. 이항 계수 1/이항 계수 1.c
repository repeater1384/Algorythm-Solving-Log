#include<stdio.h>

int fac(int n)
{
	if (n <= 1)
		return 1;
	else
		return n * fac(n - 1);
}
int main() {
	int n, k;
	scanf("%d %d", &n, &k);
	printf("%d", fac(n) / fac(k) / fac(n - k));
	return 0;
}
