N = int(input())

dp = [i for i in range(N+1)]

for i in range(1,N+1):
    # if int(i**.5) == i**.5:
    #     dp[i] = 1
    # else:
    for j in range(1,int(i**.5)+1):
        if dp[i-(j*j)]+1 < dp[i]:
            dp[i] = dp[i-(j*j)]+1
print(dp[N])
