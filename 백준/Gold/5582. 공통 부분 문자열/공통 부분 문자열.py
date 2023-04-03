str1 = input()
str2 = input()
len1 = len(str1)
len2 = len(str2)

dp = [[0] * (len1 + 1) for _ in range((len2 + 1))]

answer = 0
for i in range(1, len2 + 1):
    for j in range(1, len1 + 1):
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer,dp[i][j])

print(answer)