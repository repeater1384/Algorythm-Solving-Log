import sys
n,m = map(int,sys.stdin.readline().split())
dic = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    dic[name] = i+1
    dic[i+1] = name
for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(dic[int(q)])
    else:
        print(dic[q])