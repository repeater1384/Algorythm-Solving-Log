#include<stdio.h>


int main(a)
{
	int e,s,m;	//max =15,28,19
	
	scanf("%d %d %d", &e, &s, &m);
	
	while (1)
	{
		if (e == 1 && s == 1 && m == 1)
			break;
		a++;
		e--, s--, m--;
		if (!e)
			e = 15;
		if (!s)
			s = 28;
		if (!m)
			m = 19;
	}
	printf("%d", a);
}