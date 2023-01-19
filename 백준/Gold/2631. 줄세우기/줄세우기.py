N = int(input())
arr = [int(input()) for _ in range(N)]

# dp[i] => i번째 인덱스까지 가장 긴 증가하는 부분 수열의 길이.
dp = [-1] * N
dp[0] = 1
for i in range(1, N):
    max_val = 0
    for j in range(i):
        if arr[j] < arr[i]:
            max_val = max(max_val, dp[j])
    dp[i] = max_val + 1
print(N - max(dp))
