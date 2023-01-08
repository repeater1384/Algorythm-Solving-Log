import sys

input = sys.stdin.readline

# dp[n][i] -> n을 i를 마지막으로 해서 표현하는 가짓수
dp = [[0] * 4 for _ in range(100001)]
MOD = 1_000_000_009

dp[1][1] = 1
dp[2][2] = 1
dp[3][3] = 1
dp[3][1] = 1
dp[3][2] = 1

for n in range(4, 100001):
    dp[n][1] = (dp[n - 1][2] + dp[n - 1][3]) % MOD
    dp[n][2] = (dp[n - 2][1] + dp[n - 2][3]) % MOD
    dp[n][3] = (dp[n - 3][1] + dp[n - 3][2]) % MOD
    
print(*[sum(dp[n]) % MOD for n in [int(input()) for _ in range(int(input()))]], sep='\n')
