T, W = map(int, input().split())
arr = [int(input()) - 1 for _ in range(T)]

dp = [[0] * (W + 1) for _ in range(T)]
for w in range(arr[0], W + 1, 2):
    dp[0][w] = 1

for t in range(1, T):
    dp[t][0] = dp[t - 1][0] + (arr[t] == 0)
    for w in range(1, W + 1):
        dp[t][w] = max(dp[t - 1][w], dp[t - 1][w - 1]) + (w % 2 == arr[t])
print(max(dp[T - 1]))
