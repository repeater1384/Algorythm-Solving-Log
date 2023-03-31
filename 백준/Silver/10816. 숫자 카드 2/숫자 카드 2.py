import collections
input()
a = [*map(int,input().split())]
input()
b = [*map(int,input().split())]
k = collections.Counter(a)
for i in b:
    print(k[i],end=' ')
