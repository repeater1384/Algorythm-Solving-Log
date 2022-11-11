INF = 10 ** 6
N, M = map(int, input().split())
dis = [[INF] * (N + 1) for _ in range(N + 1)]
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    dis[a][b] = min(dis[a][b], c)
    dis[b][a] = min(dis[b][a], c)

for i in range(N + 1):
    dis[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

answer = INF
for start in range(1, N + 1):
    cur_dis = dis[start]
    cur_time = 0
    for a, b, c in edges:
        cur_time = max(cur_time, (cur_dis[a] + cur_dis[b] + c) / 2)
    answer = min(cur_time, answer)
print(answer)
