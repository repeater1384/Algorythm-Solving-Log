a = 0
k = []
for _ in range(10):
    b,c = map(int,input().split())
    a = a-b+c
    k.append(a)
print(max(k))