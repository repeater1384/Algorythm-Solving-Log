n = int(input())

s = [[0]*10 for _ in range(n+1)]
for i in range(0,10):
    s[1][i] = 1
for i in range(2,n+1):
    for j in range(10):
        for k in range(j,10):
            s[i][j] += s[i-1][k]


print(sum(s[n])%10007)