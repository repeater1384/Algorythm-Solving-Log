#include <stdio.h>
#include <stdlib.h>
int main()
{

	int N, M;
	scanf("%d %d", &N, &M);

	int *arr;
	arr = (int *)malloc(sizeof(int)*M);
	for (int i = 0; i < M; i++)
	{
		scanf("%d", &arr[i]);
	}
	//////
	int sum = 0;

	for (int i = 1; i <= N; i++)
	{
		for (int k = 0; k < M; k++)
		{
			if (i%arr[k] == 0)
			{
				sum += i;
				break;
			}
		}
	}
	printf("%d", sum);
}