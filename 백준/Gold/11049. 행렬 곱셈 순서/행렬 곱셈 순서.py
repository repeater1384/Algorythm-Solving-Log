N = int(input())
matrix = [[*map(int, input().split())] for _ in range(N)]

dp = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
for i in range(N - 1):
    dp[i][i + 1] = matrix[i][0] * matrix[i][1] * matrix[i + 1][1]

for k in range(2, N):
    # i ~ i+k 까지 채우겠다는 뜻
    for i in range(N - k):
        for j in range(i, i + k):
            start, mid, end = i, j, i + k
            dp[start][end] = min(dp[start][end],
                                 dp[start][mid] + dp[mid + 1][end] + matrix[start][0] * matrix[mid][1] * matrix[end][1])

print(dp[0][N - 1])
