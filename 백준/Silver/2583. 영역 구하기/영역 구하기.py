import sys

sys.setrecursionlimit(10 ** 6)

M, N, K = map(int, input().split())
matrix = [[False] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            matrix[y][x] = True


def dfs(_x, _y):
    global size
    size += 1
    matrix[_y][_x] = True
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for _i in range(4):
        nx, ny = _x + dx[_i], _y + dy[_i]
        if 0 <= nx < N and 0 <= ny < M:
            if not matrix[ny][nx]:
                dfs(nx, ny)
    return size


count = 0
sizes = []
for y in range(M):
    for x in range(N):
        if not matrix[y][x]:
            count += 1
            size = 0
            dfs(x, y)
            sizes.append(size)

print(count)
print(*sorted(sizes))
