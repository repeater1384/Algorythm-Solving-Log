import sys

input = sys.stdin.readline


def find_path(i, j):
    if middle[i][j] == -1:
        return []
    k = middle[i][j]
    return find_path(i, k) + [k] + find_path(k, j)


N = int(input())
M = int(input())
INF = float('inf')
adj_matrix = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(lambda x: int(x) - 1, input().split())
    adj_matrix[a][b] = min(adj_matrix[a][b], c + 1)

route = [[] * N for _ in range(N)]
middle = [[-1] * N for _ in range(N)]
for k in range(N):
    adj_matrix[k][k] = 0
    for i in range(N):
        for j in range(N):
            if adj_matrix[i][j] > adj_matrix[i][k] + adj_matrix[k][j]:
                adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
                middle[i][j] = k
answer = []
for i in range(N):
    answer.append(' '.join(map(str, map(lambda x: 0 if x == INF else x, adj_matrix[i]))))

for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] in [0, INF]:
            answer.append(0)
            continue
        route = [i] + find_path(i, j) + [j]
        answer.append(f'{len(route)} {" ".join(map(str, map(lambda x: x + 1, route)))}')

print(*answer, sep='\n')
