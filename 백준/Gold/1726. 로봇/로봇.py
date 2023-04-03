from collections import deque

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
sy, sx, sdir = map(lambda x: int(x) - 1, input().split())
ey, ex, edir = map(lambda x: int(x) - 1, input().split())

# visited[i][j][dir] => i,j 위치에 dir 방향으로 있기 위한 최솟값
visited = [[[-1] * 4 for _ in range(M)] for _ in range(N)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
ddir = {0: [2, 3], 1: [2, 3], 2: [0, 1], 3: [0, 1]}
queue = deque()
queue.append((sy, sx, sdir, 0))

while queue:
    cy, cx, cdir, cnt = queue.popleft()
    if cy == ey and cx == ex and cdir == edir:
        print(cnt)
        break
    # 앞으로 가보기
    for k in range(1, 4):
        ny, nx = cy + dy[cdir] * k, cx + dx[cdir] * k
        if 0 <= ny < N and 0 <= nx < M:
            if matrix[ny][nx] == 1:
                break
            if visited[ny][nx][cdir] == -1:
                visited[ny][nx][cdir] = cnt + 1
                queue.append((ny, nx, cdir, cnt + 1))
    # 방향 전환
    for ndir in ddir[cdir]:
        if visited[cy][cx][ndir] == -1:
            visited[cy][cx][ndir] = cnt + 1
            queue.append((cy, cx, ndir, cnt + 1))
