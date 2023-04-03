import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
cost = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            cost[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a != b:
                cost[a][b] = min(cost[a][b], cost[a][k] + cost[k][b])

for row in cost[1:]:
    print(*map(lambda x: 0 if x == float('inf') else x, row[1:]))
