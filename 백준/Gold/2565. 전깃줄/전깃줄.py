size = int(input())

power_pole = [[*map(int, input().split())] for _ in range(size)]
power_pole.sort(key=lambda x: x[0])

dp = [0] * size

for i in range(size):
    temp = 0
    for j in range(i):
        if power_pole[i][1] > power_pole[j][1]:
            temp = max(temp, dp[j])
    dp[i] = temp + 1

print(size - max(dp))
