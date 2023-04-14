N = int(input())
temp = [[*map(int, input().split())] for _ in range(N)]
temp.sort(key=lambda x: x[0])
arr = [t[1] for t in temp]
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

answer_len = N - lis_len
answer_arr = []
for i in range(N - 1, -1, -1):
    if index_arr[i] == find:
        find -= 1
    else:
        answer_arr.append(temp[i][0])

print(answer_len)
print(*answer_arr[::-1])
