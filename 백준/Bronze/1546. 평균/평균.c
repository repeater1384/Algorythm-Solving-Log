#include<stdio.h>
#include<stdlib.h>
int main()
{
	int N;
	scanf("%d", &N);

	float *arr;
	arr = (float *)(malloc(sizeof(float)*N));

	int max = 0;
	float sum = 0;
	for (int i = 0; i < N; i++)
	{
		scanf("%f", &arr[i]);
		if (max < arr[i])
			max = arr[i];
	}

	for (int i = 0; i < N; i++)
	{
		arr[i] = arr[i] / max * 100;
		sum += arr[i];
	}
	printf("%f", sum / N);
	return 0;
}