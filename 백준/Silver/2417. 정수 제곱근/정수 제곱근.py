N = int(input())
s, e = 0, 1 << 63
while s <= e:
    mid = (s + e) // 2
    if mid ** 2 >= N:
        e = mid - 1
    else:
        s = mid + 1
print(s)
