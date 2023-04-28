import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parents = [i for i in range(N + 1)]


def find(x):
    global parents
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def is_same_parents(x, y):
    return find(x) == find(y)


def union(x, y):
    global parents
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


answer = 0
cnt = 0
for x, y, cost in edges:
    if is_same_parents(x, y):
        answer += cost
        continue
    union(x, y)
    cnt += 1
print(answer if cnt == N - 1 else -1)
