N = int(input())
matrix = [[*map(int, input().split())] for _ in range(N)]
INF = float('inf')
dp = [[-1] * (1 << N) for _ in range(N)]


def dfs(cur, visited):
    if visited + 1 == 1 << N:
        if matrix[cur][0] != 0:
            return matrix[cur][0]
        return INF

    if dp[cur][visited] != -1:
        return dp[cur][visited]

    dp[cur][visited] = INF
    for i in range(N):
        if matrix[cur][i] == 0:
            continue
        if visited & (1 << i):
            continue
        dp[cur][visited] = min(dp[cur][visited], dfs(i, visited | (1 << i)) + matrix[cur][i])
    return dp[cur][visited]


print(dfs(0, 1))
