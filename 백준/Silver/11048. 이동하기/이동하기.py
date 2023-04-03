R, C = map(int, input().split())

dp = [[0] * (C + 1) for _ in range(R + 1)]
matrix = [[0] * (C + 1)]
for _ in range(R):
    matrix.append([0] + [*map(int, input().split())])

for y in range(1, R + 1):
    for x in range(1, C + 1):
        dp[y][x] = matrix[y][x] + max(dp[y-1][x],dp[y][x-1])

print(dp[R][C])