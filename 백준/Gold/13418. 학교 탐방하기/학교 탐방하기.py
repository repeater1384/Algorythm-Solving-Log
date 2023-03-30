import sys

input = sys.stdin.readline


def find(x):
    global parents
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    global parents
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


N, M = map(int, input().split())
edges = [[*map(int, input().split())] for _ in range(M + 1)]
min_answer, max_answer = 0, 0

parents = [i for i in range(N + 1)]
for edge in sorted(edges, key=lambda x: -x[2]):
    a, b, c = edge
    if find(a) == find(b):
        continue
    union(a, b)
    min_answer += c == 0

parents = [i for i in range(N + 1)]
for edge in sorted(edges, key=lambda x: x[2]):
    a, b, c = edge
    if find(a) == find(b):
        continue
    union(a, b)
    max_answer += c == 0

print(max_answer ** 2 - min_answer ** 2)
