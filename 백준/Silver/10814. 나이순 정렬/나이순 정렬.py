a = []
for _ in range(int(input())):
    a.append(input().split())
a.sort(key = lambda x:int(x[0]))
for k in a:
    print(*k)