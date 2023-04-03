N = int(input())
dp = [0, 1, 1, 2, 2, 1, 2, 1]

if N > 7:
    dp += [0] * (N - 7)
    for i in range(8, N+1):
        dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 5], dp[i - 7]) + 1
# print(dp)
print(dp[N])