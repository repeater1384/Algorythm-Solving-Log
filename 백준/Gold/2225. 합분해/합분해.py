N, K = map(int, input().split())

# K개의 정수를 더해서 N을 만들기

# dp[n][k] k개의 수로 n을 만드는 경우의 수
dp = [[0] * (K + 1) for _ in range(N + 1)]

# n = 5 , k = 3
# dp[0][1] = 1
# dp[1][2] -> dp[1][1] + dp[0][1]   / 1 , 0 / 1+0, 0+1
# dp[1][3] -> dp[1][2] + dp[0][2]   / 1+0, 0+1 / 0+0
# dp[2][3] -> dp[2][2] + dp[1][2] + dp[
for n in range(N + 1):
    for k in range(1, K + 1):
        # 숫자 1개만 쓰면 1개만 나옴
        if k == 1:
            dp[n][k] = 1
        else:
            for t in range(n + 1):
                dp[n][k] += dp[t][k - 1]
            dp[n][k] %= 1_000_000_000
print(dp[N][K])
