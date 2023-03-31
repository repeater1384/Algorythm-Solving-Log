N = int(input())
MOD = 1_000_000_000
MAX = 1 << 10
# dp[i][3]['0000111101'] -> i자리 이면서 3으로 끝나고, 0,3,4,5,6이 포함된 계단수의 개수.
dp = [[[0] * MAX for _ in range(10)] for _ in range(N + 1)]
for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for bit in range(MAX):
            if dp[i - 1][j][bit]:
                if j > 0:
                    dp[i][j - 1][bit | (1 << (j - 1))] += dp[i - 1][j][bit]
                if j < 9:
                    dp[i][j + 1][bit | (1 << (j + 1))] += dp[i - 1][j][bit]
                    
print(sum(dp[N][i][MAX - 1] for i in range(10)) % MOD)
