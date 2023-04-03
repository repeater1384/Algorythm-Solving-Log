V, E = map(int, input().split())
INF = 1e9
adj_matrix = [[INF] * V for _ in range(V)]
for _ in range(E):
    a, b, c = map(lambda x: int(x) - 1, input().split())
    adj_matrix[a][b] = c + 1

for k in range(V):
    for i in range(V):
        for j in range(V):
            adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])
answer = INF
for i in range(V):
    answer = min(answer, adj_matrix[i][i])
print(-1 if answer == INF else answer)
