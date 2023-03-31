dp = [False] * 1001
dp[1] = dp[3] = dp[4] = True
for i in range(5, 1001):
    dp[i] = not all((dp[i - 1], dp[i - 3], dp[i - 4]))
N = int(input())
print('SK' if dp[N] else 'CY')
