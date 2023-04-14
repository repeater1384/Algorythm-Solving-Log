N = int(input())

matrix = [[*map(int, input().split())] for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for y in range(N):
    for x in range(N):
        jump = matrix[y][x]
        if x == y == N - 1:
            print(dp[y][x])
            break

        if jump + x < N:
            dp[y][x + jump] += dp[y][x]
        if jump + y < N:
            dp[y + jump][x] += dp[y][x]

# for row in dp:
#     print(row)
