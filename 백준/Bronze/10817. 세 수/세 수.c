#include <stdio.h>

int main() {

	int arr[3], i, j, tmp;

	scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);

	for(i=0; i<3; i++)

		for(j=0; j<2; j++)

			if(arr[j] >= arr[j+1]) {

				tmp = arr[j];

				arr[j] = arr[j+1];

				arr[j+1] = tmp;

			}

	printf("%d\n", arr[1]);

	return 0;

}
