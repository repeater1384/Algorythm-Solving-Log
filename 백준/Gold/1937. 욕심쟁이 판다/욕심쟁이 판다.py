import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
matrix = [[*map(int, input().split())] for _ in range(N)]

dp = [[0] * N for _ in range(N)]
di, dj = [0, 0, 1, -1], [1, -1, 0, 0]


def dfs(i, j):
    res = [1]
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and matrix[i][j] < matrix[ni][nj]:
            if dp[ni][nj] != 0:
                res.append(dp[ni][nj] + 1)
            else:
                res.append(dfs(ni, nj) + 1)

    dp[i][j] = max(res)
    return dp[i][j]


for i in range(N):
    for j in range(N):
        if dp[i][j] == 0:
            dfs(i, j)
print(max(max(row) for row in dp))
