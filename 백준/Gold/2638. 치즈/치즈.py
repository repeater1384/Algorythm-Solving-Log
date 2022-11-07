from collections import deque

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def melt():
    visited = [[False] * M for _ in range(N)]
    touch_air = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        cy, cx = queue.popleft()
        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if matrix[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                if matrix[ny][nx] == 1:
                    touch_air[ny][nx] += 1

    for i in range(N):
        for j in range(M):
            if touch_air[i][j] >= 2:
                matrix[i][j] = 0


answer = 0
while True:
    if sum([sum(row) for row in matrix]) == 0:
        break
    melt()
    answer += 1

print(answer)
