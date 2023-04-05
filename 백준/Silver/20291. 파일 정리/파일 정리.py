import sys

input = sys.stdin.readline
N = int(input())

data = {}
for _ in range(N):
    _, name = input().rstrip().split('.')
    data[name] = data.get(name, 0) + 1

for key in sorted(data.keys()):
    print(key, data[key])
