import sys

input = sys.stdin.readline
N, M, T = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parents = [i for i in range(N + 1)]


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def is_same_parents(x, y):
    return find(x) == find(y)


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


cnt = 0
answer = 0
for x, y, cost in edges:
    if not is_same_parents(x, y):
        answer += cost + T * cnt
        cnt += 1
        union(x, y)
print(answer)
