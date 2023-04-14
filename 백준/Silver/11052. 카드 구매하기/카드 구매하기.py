n= int(input())
card = [0]+[*map(int,input().split())]
dp = [0] * (n+1)

for i in range(1,n+1):
    if i == 1:
        dp[i] = card[i]
    else:
        for j in range(1,i+1):
            dp[i] = max(dp[i],dp[i-j]+card[j])

print(dp[-1])
