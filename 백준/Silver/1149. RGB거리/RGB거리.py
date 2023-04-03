RGB = [[0]*3 for _ in range(int(input()))]
for i in range(len(RGB)):
    RGB[i] = [*map(int,input().split())]
DP = [[0]*3 for _ in range(len(RGB))]
DP[0] = RGB[0]
for i in range(1,len(RGB)):
    DP[i][0] = RGB[i][0] + min(DP[i-1][1],DP[i-1][2])
    DP[i][1] = RGB[i][1] + min(DP[i-1][0],DP[i-1][2])
    DP[i][2] = RGB[i][2] + min(DP[i-1][0],DP[i-1][1])
print(min(DP[-1]))