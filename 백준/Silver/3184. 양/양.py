import sys
sys.setrecursionlimit(10**6)


R, C = map(int, input().split())

matrix = [[*input()] for _ in range(R)]
visit = [[False] * C for _ in range(R)]


def dfs(cx, cy):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visit[cy][cx] = True
    global n_sheep, n_wolf
    for dx, dy in d:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < C and 0 <= ny < R and not visit[ny][nx]:
            if matrix[ny][nx] == "#":
                continue
            elif matrix[ny][nx] == "o":
                n_sheep += 1
            elif matrix[ny][nx] == "v":
                n_wolf += 1
            dfs(nx, ny)


answer_sheep, answer_wolf = 0, 0
for y in range(R):
    for x in range(C):
        if not visit[y][x]:
            n_sheep, n_wolf = 0, 0
            dfs(x, y)

            if n_sheep > n_wolf:
                answer_sheep += n_sheep
            else:
                answer_wolf += n_wolf

print(answer_sheep, answer_wolf)
