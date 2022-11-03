N = int(input())
K = int(input())
MOD = 1_000_000_003


def dfs(n, k):
    global dp
    if k == 1:
        return n
    if n / k == 2:
        return 2
    if dp[n][k] == 0:
        dp[n][k] = dfs(n - 1, k) + dfs(n - 2, k - 1)
    return dp[n][k]


dp = [[0] * (K + 1) for _ in range(N + 1)]
print(0 if N / K < 2 else dfs(N, K) % MOD)
