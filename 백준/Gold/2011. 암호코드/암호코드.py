data = input()
dp = [0] * (len(data))

flag = True
for i in range(len(data)):
    if i == 0:
        if data[i] == '0':
            flag = False
        else:
            dp[i] = 1
    elif i == 1:
        if data[i] == '0':
            if data[i - 1] == '1' or data[i - 1] == '2':
                dp[i] = 1
            else:
                flag = False
        else:
            if int(data[i - 1:i + 1]) <= 26 :
                dp[i] = 2
            else:
                dp[i] = 1
    else:
        if data[i] == '0':
            if data[i - 1] == '1' or data[i - 1] == '2':
                dp[i] = dp[i - 2]
            else:
                flag = False
        elif int(data[i - 1:i + 1]) <= 26 and data[i - 1] != '0':
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1]
    dp[i] %= 1000000

print(dp[len(data) - 1] if flag else 0)
