N = int(input())
arr = [*map(int, input().split())]
index_arr = [0] * N
dp = [-float('inf')]


def lower_bound(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


for i in range(N):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        index_arr[i] = len(dp) - 1
    else:
        idx = lower_bound(dp, arr[i])
        dp[idx] = arr[i]
        index_arr[i] = idx

lis_len = len(dp) - 1
find = lis_len
lis_arr = []

for i in range(N - 1, -1, -1):
    if find == 0:
        break
    if index_arr[i] == find:
        lis_arr.append(arr[i])
        find -= 1

print(lis_len)
print(*lis_arr[::-1])
