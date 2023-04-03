#include<stdio.h>
#include<math.h>
int main()
{
	int n;
	scanf("%d", &n);
	int arr[10] = { 0 };
	
	while (n > 0)
	{
		arr[n%10]++;
		n /= 10;
	}
	arr[6] =ceil((arr[6] + arr[9])/2.0);
	arr[9] = 0;

	int max = 0;
	for (int i = 0; i < 10; i++)
	{
		if (arr[i] > max)
			max = arr[i];
	}
	printf("%d", max);
}