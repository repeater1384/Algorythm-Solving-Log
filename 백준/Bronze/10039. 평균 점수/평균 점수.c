#include <stdio.h>

int main()
{
	int arr[5];
	int total = 0;
	scanf("%d %d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3], &arr[4]);

	for (int i = 0;i<5; i++) {
		if (arr[i] < 40) 
			arr[i] = 40;
		total += arr[i];
	}

	printf("%d", total / 5);
	

	return 0;
}