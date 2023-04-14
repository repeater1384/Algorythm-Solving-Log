N = int(input())
arr = [-1] + [*map(int, input().split())]
dp = [0] + [0] * N
for i in range(1, N + 1):
    dp[i] = max([dp[idx] for idx, prev in enumerate(arr[:i]) if arr[i] > prev]) + 1
    
print(max(dp))
