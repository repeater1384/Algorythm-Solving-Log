n= int(input())
card = [0]+[*map(int,input().split())]
dp = card.copy()

for i in range(1,n+1):
    if i == 1:
        dp[i] = card[i]
    else:
        for j in range(1,i):
            dp[i] = min(dp[i],dp[i-j]+card[j])

print(dp[-1])
