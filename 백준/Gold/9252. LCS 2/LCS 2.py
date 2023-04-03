str1 = input()
str2 = input()
len1 = len(str1)
len2 = len(str2)

dp = [[0] * (len1 + 1) for _ in range((len2 + 1))]

for i in range(1, len2 + 1):
    for j in range(1, len1 + 1):
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

i, j = len2, len1
LCS = ''

while True:
    if i == 0 or j == 0:
        break
        
    if str2[i - 1] == str1[j - 1]:
        LCS += str2[i - 1]
        i -= 1
        j -= 1
        
    else:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1
            
            
print(dp[len2][len1])
print(LCS[::-1])
