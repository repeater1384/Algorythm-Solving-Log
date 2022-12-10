def bisect_left(arr, n):
    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] < n:
            s = m + 1
        else:
            e = m - 1
    return e + 1


def bisect_right(arr, n):
    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] <= n:
            s = m + 1
        else:
            e = m - 1
    return e + 1


def get_powerset_sum(arr):
    n = len(arr)
    res = []
    for i in range(1 << n):
        temp = 0
        for j in range(n):
            if i & (1 << j) != 0:
                temp += arr[j]
        res.append(temp)
    return res


N, S = map(int, input().split())
arr = [*map(int, input().split())]

left, right = arr[:N // 2], arr[N // 2:]
left_sum = get_powerset_sum(left)
right_sum = get_powerset_sum(right)
right_sum.sort()

answer = -1 if S == 0 else 0
for l in left_sum:
    answer += bisect_right(right_sum, S - l) - bisect_left(right_sum, S - l)
    
print(answer)
