import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = [0] + [*map(int, input().split())]
    prefix_sum = [0] * (N + 1)
    dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
        dp[i][i] = 0

    for size in range(2, N + 1):
        for start in range(1, N - size + 2):
            end = start + size - 1
            dp[start][end] = min([dp[start][mid] + dp[mid + 1][end] for mid in range(start, end)]) + prefix_sum[end] - \
                             prefix_sum[start - 1]
    print(dp[1][N])
