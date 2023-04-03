N = int(input())

arr = [[' '] * (N * 2) for _ in range(N)]


def dfs(depth, x, y):
    if depth == 3:
        arr[y][x], arr[y + 1][x - 1], arr[y + 1][x + 1] = '*', '*', '*'
        for dx in range(-2, 3):
            arr[y + 2][x + dx] = '*'
    else:
        dfs(depth // 2, x, y)
        dfs(depth // 2, x - depth // 2, y + depth // 2)
        dfs(depth // 2, x + depth // 2, y + depth // 2)


dfs(N, N, 0)
for row in arr:
    print(''.join(row[1:]))
