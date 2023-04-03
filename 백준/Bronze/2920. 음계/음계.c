#include <stdio.h>

int main()
{
	int arr[8];
	int ascending = 0, descending = 0;

	for (int i = 0; i < 8; i++) {
		scanf("%d", arr + i);
		if (arr[i] == i + 1)
			ascending++;
		if (arr[i] == 8 - i)
			descending++;
	}
	
	if (ascending == 8)
		printf("ascending");
	else if (descending == 8)
		printf("descending");
	else
		printf("mixed");

	return 0;
}