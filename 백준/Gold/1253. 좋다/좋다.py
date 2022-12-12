def bisect_left(arr, n):
    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] < n:
            s = m + 1
        else:
            e = m - 1
    return s


def bisect_right(arr, n):
    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] <= n:
            s = m + 1
        else:
            e = m - 1
    return s


N = int(input())
arr = [*map(int, input().split())]
arr.sort()
check = [False] * N
for i in range(N - 1):
    for j in range(i + 1, N):
        # arr[i]와 arr[j]의 합이 되는 수를 찾는다
        val = arr[i] + arr[j]
        s, e = bisect_left(arr, val), bisect_right(arr, val)
        if s == e:
            continue
        for k in range(s, e):
            if k == i or k == j:
                continue
            check[k] = True
print(sum(check))
