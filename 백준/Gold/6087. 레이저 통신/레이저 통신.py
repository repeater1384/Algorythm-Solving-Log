from collections import deque

M, N = map(int, input().split())
matrix = [[*input()] for _ in range(N)]

flag_point = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'C':
            flag_point.append((i, j))
sy, sx = flag_point[0]
ey, ex = flag_point[1]
# i, j 까지 도달하기 거울의 최솟값
visited = [[float('inf')] * M for _ in range(N)]

queue = deque()
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
for k in range(4):
    ny, nx = sy + dy[k], sx + dx[k]
    if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] != '*':
        queue.append((ny, nx, k, 0))
        visited[ny][nx] = 0
visited[sy][sx] = 0

while queue:
    cy, cx, cd, dis = queue.popleft()
    for k in range(4):
        if abs(cd - k) == 2:
            continue
        ny, nx, ndis = cy + dy[k], cx + dx[k], dis
        if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] != '*':
            if cd != k:
                ndis += 1
            if visited[ny][nx] >= ndis:
                visited[ny][nx] = ndis
                queue.append((ny, nx, k, ndis))

print(visited[ey][ex])
