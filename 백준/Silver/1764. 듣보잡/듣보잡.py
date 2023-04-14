n,m=map(int,input().split())
a=set()
b=set()
for _ in range(n):
    a.add(input())
for _ in range(m):
    b.add(input())
print(len(a&b),*sorted(list(a&b)),sep='\n')