data = input()
N = len(data)

is_pal = [[False] * N for _ in range(N)]
for i in range(N):
    is_pal[i][i] = True
for i in range(N - 1):
    is_pal[i][i + 1] = data[i] == data[i + 1]
for k in range(2, N):
    for i in range(N - k):
        is_pal[i][i + k] = data[i] == data[i + k] and is_pal[i + 1][i + k - 1]

dp = [0] * (N + 1)
for end in range(N):
    dp[end] = dp[end - 1] + 1
    for start in range(end + 1):
        if is_pal[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)

print(dp[N - 1])
