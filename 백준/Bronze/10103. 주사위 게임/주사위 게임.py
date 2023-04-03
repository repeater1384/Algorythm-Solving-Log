n = int(input())
a,b = 100,100
for _ in range(n):
    x,y = map(int,input().split())
    if x > y:
        b -= x
    if y > x:
        a -= y
print(a)
print(b)