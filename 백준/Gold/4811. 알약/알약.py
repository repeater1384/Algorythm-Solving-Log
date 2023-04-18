dp = [[0] * 31 for _ in range(31)]

for w in range(31):
    for h in range(31):
        if w < h:
            continue
        if h == 0:
            dp[w][h] = 1
        else:
            dp[w][h] = dp[w - 1][h] + dp[w][h - 1]
while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N][N])