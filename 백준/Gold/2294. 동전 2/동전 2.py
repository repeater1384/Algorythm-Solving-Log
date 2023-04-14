n, k = map(int, input().split())

coins = sorted(int(input()) for _ in range(n))
dp = [0] + [-1] * k
for c in coins:
    if c <= k:
        dp[c] = 1

for i in range(1, k + 1):
    temp = []
    for c in coins:
        if i >= c and dp[i - c] != -1:
            temp.append(dp[i - c])
    if temp:
        dp[i] = min(temp) + 1

print(dp[k])
