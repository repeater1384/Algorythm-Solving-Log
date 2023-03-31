N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]


def bisect_left(k):
    # k가 들어갈 가장 작은 index를 찾음
    s, e = 0, N - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] < k:
            s = m + 1
        else:
            e = m - 1
    return s


arr.sort()
answer = float('inf')
for num in arr:
    target = num + M
    target_idx = bisect_left(target)
    if target_idx == N:
        break
    answer = min(answer, arr[target_idx] - num)
print(answer)
