import itertools as c
n,m = map(int,input().split(' '))
for k in list(c.combinations_with_replacement([i+1 for i in range(n)],m)):
    for i in k:print(i,end=' ')
    print()