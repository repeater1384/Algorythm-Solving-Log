#include<stdio.h>
#include<stdlib.h>
int main()
{
	int size;
	int *arr;
	scanf("%d", &size);
	arr = (int *)(malloc(size * sizeof(int)));
	for (int i = 0; i < size; i++)
	{
		scanf("%d", &arr[i]);
	}

	for (int i = 0; i < size - 1; i++)
	{
		for (int j = 0; j < size - 1 - i; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				arr[j] = arr[j] ^ arr[j + 1];
				arr[j+1] = arr[j] ^ arr[j + 1];
				arr[j] = arr[j] ^ arr[j + 1];
			}
		}
	}

	for (int i = 0; i < size; i++)
	{
		printf("%d\n",arr[i]);
	}
}
