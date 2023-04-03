#include<stdio.h>
int main()
{
	int x, y, w, h;
	scanf("%d %d %d %d", &x, &y, &w, &h);
	int arr[4];
	arr[0] = x;
	arr[1] = y;
	arr[2] = w - x;
	arr[3] = h - y;
	int min = arr[0];
	for (int i = 0; i < 4; i++)
	{
		if (min > arr[i])
			min = arr[i];
	}

	printf("%d", min);
}
