N = int(input())
arr = [*map(int, input().split())]
dp = [[-float('inf')] * 2 for _ in range(N)]
dp[0][0] = arr[0]
dp[0][1] = -float('inf')
for i in range(1, N):
    dp[i][0] = max(dp[i - 1][0], 0) + arr[i]
    dp[i][1] = max(max(dp[i - 1][1], 0) + arr[i], dp[i - 1][0])

print(max(map(max, dp)))