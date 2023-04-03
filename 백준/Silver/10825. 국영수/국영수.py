import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    name, a, b, c = input().split()
    a, b, c = map(int, [a, b, c])
    arr.append([name,a,b,c])

arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for n,*_ in arr:
    print(n)