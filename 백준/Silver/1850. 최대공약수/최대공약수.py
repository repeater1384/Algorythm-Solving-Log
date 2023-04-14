import math
a,b=map(int,input().split())
for _ in range(min(math.gcd(a,b),a,b)):
    print('1',end='')