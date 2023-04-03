#include<stdio.h>


int main()
{
	int a = 3;
	int d;
	int x;
	while (a--)
	{
		d = 0;
		for (int i = 0; i < 4; i++)
		{
			scanf("%d", &x);
			if (x == 1)
				d++;
		}
		switch (d)
		{
		case 0: printf("D\n"); break;
		case 1: printf("C\n"); break;
		case 2: printf("B\n"); break;
		case 3: printf("A\n"); break;
		case 4: printf("E\n"); break;
		}
			

	}
}