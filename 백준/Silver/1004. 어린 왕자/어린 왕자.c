#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main()

{
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)

	{
		int count = 0;

		int x1, y1, x2, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

		int n;
		scanf("%d", &n);

		for (int x = 0; x < n; x++)
		{
			int cx, cy, r;
			scanf("%d %d %d", &cx, &cy, &r);

			bool in1 = pow(cx - x1, 2) + pow(cy - y1, 2) < pow(r, 2) ? true : false
				, in2 = pow(cx - x2, 2) + pow(cy - y2, 2) < pow(r, 2) ? true : false;

			if (in1 != in2) count++;
		}
		printf("%d\n", count);

	}

	return 0;
}
