N, S, M = map(int, input().split())
arr = [*map(int, input().split())]

dp = [set() for _ in range(N + 1)]
dp[0].add(S)
for i in range(N):
    for cur in dp[i]:
        if cur + arr[i] <= M:
            dp[i + 1].add(cur + arr[i])
        if 0 <= cur - arr[i]:
            dp[i + 1].add(cur - arr[i])
print(max(dp[N]) if dp[N] else -1)
