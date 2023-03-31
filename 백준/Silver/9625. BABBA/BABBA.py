K = int(input())

dp = [[0, 0] for _ in range(K + 1)]

dp[0][0] = 1

for i in range(K):
    a, b = dp[i]
    dp[i+1][0] = b
    dp[i+1][1] = b + a

print(*dp[K])
