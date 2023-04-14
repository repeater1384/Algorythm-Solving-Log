import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == 1 or (graph[a][k] + graph[k][b] == 2):
                graph[a][b] = 1

answer = 0
for i in range(1, n + 1):
    known = -1
    for j in range(1, n + 1):
        known += graph[i][j] + graph[j][i]

    if known == n:
        answer += 1

print(answer)
