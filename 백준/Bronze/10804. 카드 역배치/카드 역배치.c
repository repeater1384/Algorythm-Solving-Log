#include<stdio.h>
#include<stdlib.h>

void shuffle(int *arr, int a, int b)
{
	int *temp = (int *)(malloc(21 * sizeof(int)));

	for (int i = a; i <= b; i++)
	{
		temp[i] = arr[i];
	}

	for (int i = a, j = b; i <= b; i++, j--)
	{
		arr[i] = temp[j];
	}
	free(temp);
}

int main()
{
	int *arr = (int *)(malloc(21 * sizeof(int)));
	for (int i = 0; i <= 20; i++)
	{
		arr[i] = i;
	}

	int r = 10;
	int a, b;

	while (r--)
	{
		scanf("%d %d", &a, &b);
		shuffle(arr, a, b);
	}

	for (int i = 1; i <= 20; i++)
	{
		printf("%d ", arr[i]);
	}
}