def bisect_left(arr, target):
    s, e = 0, M - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] < target:
            s = m + 1
        else:
            e = m - 1
    return s


def bisect_right(arr, target):
    s, e = 0, M - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] <= target:
            s = m + 1
        else:
            e = m - 1
    return s


M, N, L = map(int, input().split())
guns = [*map(int, input().split())]
answer = 0
guns.sort()
for _ in range(N):
    x, y = map(int, input().split())
    left = bisect_left(guns, x)
    right = bisect_right(guns, x)
    if right - left == 1 and y <= L:
        answer += 1
        continue
    for i in (left - 1, left):
        if i < 0:
            continue
        if abs(x - guns[i]) + y <= L:
            answer += 1
            break
print(answer)