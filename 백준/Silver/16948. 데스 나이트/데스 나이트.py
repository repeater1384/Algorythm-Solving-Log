from collections import deque

N = int(input())

y1, x1, y2, x2 = map(int, input().split())

visited = [[False] * N for _ in range(N)]
dy, dx = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

queue = deque()
queue.append((y1, x1, 0))
visited[y1][x1] = True
answer = -1
while queue:
    cy, cx, cnt = queue.popleft()
    if cy == y2 and cx == x2:
        answer = cnt
        break
    for k in range(6):
        ny, nx = cy + dy[k], cx + dx[k]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            visited[ny][nx] = True
            queue.append((ny, nx, cnt + 1))

print(answer)
