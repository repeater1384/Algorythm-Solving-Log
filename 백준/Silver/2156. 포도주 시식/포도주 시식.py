import sys

input = sys.stdin.readline

n = int(input())
grape = [0] + [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(grape))
else:
    dp = [0] * (n + 1)
    dp[1] = grape[1]
    dp[2] = grape[1] + grape[2]
    for i in range(3, n + 1):
        dp[i] = max(grape[i] + grape[i - 1] + dp[i - 3], grape[i] + dp[i - 2], dp[i - 1])

    print(dp[n])
