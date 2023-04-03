#include<stdio.h>

int gcd(int a, int b)
{
	int r;
	if (a < b)
	{
		a = a ^ b;
		b = a ^ b;
		a = a ^ b;

	}

	while (b != 0)
	{
		r = a % b;
		a = b;
		b = r;
	}
	return a;
}
int lcm(int a, int b)
{
	int i, j;
	j = a < b ? b : a;

	for (i = j;; i++)
		if (i % a == 0 && i % b == 0)
			return i;
}
int main()
{
	int N, P;

	scanf("%d %d", &N, &P);
	printf("%d\n%d", gcd(N,P), lcm(N,P));

	//printf("%d %d", N / GCD(N, P), P / GCD(N, P));


	return 0;
}