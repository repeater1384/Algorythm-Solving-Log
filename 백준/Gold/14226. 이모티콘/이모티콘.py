import sys
sys.setrecursionlimit(100000)
S = int(input())
N = S * 2 + 2
dp = [float('inf')] * N


def dfs(cur, cnt):
    dp[cur] = cnt

    if cur * 2 < N and dp[cur * 2] > cnt + 2:
        dfs(cur * 2, cnt + 2)
    if cur - 1 > 0 and dp[cur - 1] > cnt + 1:
        dfs(cur - 1, cnt + 1)
    d = 2
    for next_cur in range(cur * 2, N, cur):
        if dp[next_cur] > cnt + d:
            dfs(next_cur, cnt + d)
        d += 1


dfs(1, 0)
print(dp[S])
