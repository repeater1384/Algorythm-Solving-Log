N = int(input())

A = [*map(int, input().split())]

dp = [0] * N
for i in range(N):
    temp = 0

    for j in range(i):
        if A[i] > A[j]:
            temp = max(temp, dp[j])

    dp[i] = temp + A[i]
    
print(max(dp))
