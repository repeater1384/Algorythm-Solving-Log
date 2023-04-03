from itertools import *
n=int(input())
for k in permutations(range(1,n+1),n):
    print(*k)