N = int(input())

dp = [1, 0, 3] + [0] * 28

for i in range(4, N + 1, 2):
    dp[i] = dp[i - 2] * 3
    for j in range(4, i + 1, 2):
        dp[i] += dp[i - j] * 2
        
print(dp[N])
