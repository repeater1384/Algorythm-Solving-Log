#include<stdio.h>
n;
int temp[42];
int main()
{
	int arr[10];
	for (int i = 0; i < 10; i++)
	{
		scanf("%d", &arr[i]);
		temp[arr[i] % 42] = 1;
	}
	for (int i = 0; i < 42; i++)
	{
		if (temp[i])
			n++;
	}
	printf("%d", n);
	
}