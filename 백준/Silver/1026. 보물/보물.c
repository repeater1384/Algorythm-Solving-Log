#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
	return *(int*)a - *(int*)b;
}

int main() {
	int N;
	scanf("%d", &N);
	int* A = (int*)malloc(sizeof(int) * N);
	int* B = (int*)malloc(sizeof(int) * N);

	for (int i = 0; i < N; i++) {
		scanf("%d", A + i);
	}

	for (int i = 0; i < N; i++) {
		scanf("%d", B + i);
	}

	qsort(A, N, sizeof(int), compare);
	qsort(B, N, sizeof(int), compare);

	int answer = 0;
	for (int i = 0; i < N; i++) {
		answer += A[i] * B[N - i - 1];
	}

	printf("%d", answer);
	free(A);
	free(B);

}