#include <stdio.h>


int main() {
	int l,p,v;
	int idx = 1;
	while (1) {
		scanf("%d %d %d", &l, &p, &v);
		if (l == 0 && p == 0 && v == 0) {
			break;
		}

		printf("Case %d: %d\n", idx++, (v / p) * l + ((v % p) >= l ? l : (v % p) ));
		
	}
	return 0;
}
