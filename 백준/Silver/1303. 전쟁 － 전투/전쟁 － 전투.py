M, N = map(int, input().split())
matrix = [[*input()] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
di, dj = [-1, 1, 0, 0], [0, 0, 1, -1]


def dfs(i, j, color):
    visited[i][j] = True
    result = 1
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and matrix[ni][nj] == color:
            result += dfs(ni, nj, color)
    return result


result = {'W': 0, 'B': 0}
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            result[matrix[i][j]] += dfs(i, j, matrix[i][j]) ** 2
print(result['W'], result['B'])
