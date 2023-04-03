#include<stdio.h>


int main()
{
	int T, H, W, N;
	int X, Y;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d %d %d", &H, &W, &N);

		Y = N % H == 0 ? H : N % H;
		X = N % H == 0 ? N / H : N / H + 1;
		printf("%d", Y);
		printf("%02d", X);
		if (T > 0)
			printf("\n");
	}
}
