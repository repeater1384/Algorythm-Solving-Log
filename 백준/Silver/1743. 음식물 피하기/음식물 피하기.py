N, M, K = map(int, input().split())
matrix = [['.' for _ in range(M)] for _ in range(N)]
visit = [[True] * M for _ in range(N)]

for _ in range(K):
    r, c = map(lambda x: int(x) - 1, input().split())
    matrix[r][c] = '#'
    visit[r][c] = False


def dfs(sx, sy):
    stack = [(sx, sy)]
    visit[sy][sx] = True
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    depth = 0
    while stack:
        cx, cy = stack.pop()
        depth += 1

        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N and not visit[ny][nx]:
                stack.append((nx, ny))
                visit[ny][nx] = True

    return depth


max_depth = -1

for y in range(N):
    for x in range(M):
        if not visit[y][x]:
            depth = dfs(x, y)
            max_depth = max(depth, max_depth)

print(max_depth)
