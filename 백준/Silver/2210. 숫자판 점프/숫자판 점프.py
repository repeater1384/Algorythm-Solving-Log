# 2210

matrix = [[*map(int, input().split())] for _ in range(5)]
result = set()


def dfs(cur_status, depth, cx, cy):
    global result
    if depth == 6:
        result.add(''.join(map(str, cur_status)))
        return

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in d:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(cur_status + [matrix[ny][nx]], depth + 1, nx, ny)


for i in range(5):
    for j in range(5):
        dfs([], 0, i, j)
print(len(result))
