N, M, R = map(int, input().split())
items = [0] + [*map(int, input().split())]
adj_matrix = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for _ in range(R):
    a, b, c = map(int, input().split())
    adj_matrix[a][b] = c
    adj_matrix[b][a] = c

for k in range(N + 1):
    adj_matrix[k][k] = 0
    for i in range(N + 1):
        for j in range(N + 1):
            adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])

answer = 0
for i in range(1, N + 1):
    temp = 0
    for j in range(1, N + 1):
        if adj_matrix[i][j] <= M:
            temp += items[j]
    answer = max(answer, temp)
print(answer)
