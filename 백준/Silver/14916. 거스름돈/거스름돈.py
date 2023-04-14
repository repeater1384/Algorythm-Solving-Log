N = int(input())
if N == 1 or N == 3:
    print(-1)
else:
    dp = [0] * 100001
    dp[1:6] = [100000, 1, 100000, 2, 1]
    for i in range(6, N + 1):
        dp[i] = min(dp[i - 2], dp[i - 5]) + 1
    print(dp[N])
