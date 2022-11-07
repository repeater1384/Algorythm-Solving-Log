import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [False] * (N + 1)
# dp[N][0] -> 일반인일때.
# dp[N][1] -> 어답터일때.
dp = [[0, 0] for _ in range(N + 1)]


def dfs(cur):
    visited[cur] = True
    dp[cur][1] = 1
    if adj_list[cur]:
        for next in adj_list[cur]:
            if visited[next]:
                continue
            dfs(next)
            dp[cur][0] += dp[next][1]
            dp[cur][1] += min(dp[next][0], dp[next][1])


dfs(1)
print(min(dp[1][0],dp[1][1]))


