N = int(input())
adj_list = {}
dp = [0] * (N + 1)
for i in range(1, N + 1):
    a, b, *c = map(int, input().split())
    adj_list[i] = c
    dp[i] = a
    
for i in range(1, N + 1):
    dp[i] += max(map(lambda x: dp[x], adj_list[i] + [0]))
    
print(max(dp))
