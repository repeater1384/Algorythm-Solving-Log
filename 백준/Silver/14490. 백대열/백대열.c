#include<stdio.h>
#include<math.h>

int gcd(int a, int b) {

	while (b != 0) {
		int temp = a % b;
		a = b;
		b = temp;
	}

	return abs(a);
}

int main()
{
	int a, b;
	scanf("%d:%d", &a, &b);
	printf("%d:%d", a / gcd(a, b), b / gcd(a, b));
}