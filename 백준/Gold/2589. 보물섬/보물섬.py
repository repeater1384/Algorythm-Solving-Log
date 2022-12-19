from collections import deque

N, M = map(int, input().split())
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
matrix = [[*input()] for _ in range(N)]


def bfs(i, j):
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((i, j, 0))
    visited[i][j] = True
    res = 0
    while queue:
        y, x, cnt = queue.popleft()
        res = max(res, cnt)
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and matrix[ny][nx] == 'L':
                visited[ny][nx] = True
                queue.append((ny, nx, cnt + 1))
    return res


answer = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)
