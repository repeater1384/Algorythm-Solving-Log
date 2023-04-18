#include<stdio.h>
#include<stdlib.h>

int getDigit(int N)
{
	int digit = 0;
	while (N > 0)
	{
		N /= 10;
		digit++;
	}
	return digit;
}
int main()
{
	int N;
	scanf("%d", &N);
	int size = getDigit(N);


	int *arr;
	arr = (int *)(malloc(size * sizeof(int)));

	for (int i = 0; i < size; i++)
	{
		arr[i] = N % 10;
		N /= 10;
	}

	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size - 1 - i; j++) {
			if (arr[j] < arr[j + 1])
			{
				arr[j] = arr[j] ^ arr[j + 1];
				arr[j+1] = arr[j] ^ arr[j + 1];
				arr[j] = arr[j] ^ arr[j + 1];
			}
		}
	}

	for (int i = 0; i < size; i++)
	{
		printf("%d", arr[i]);
	}
}
