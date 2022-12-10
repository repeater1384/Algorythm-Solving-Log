def bisect_right(arr, n):
    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] <= n:
            s = m + 1
        else:
            e = m - 1
    return s


N, M, K = map(int, input().split())
arr = sorted(map(int, input().split()))
answer = []
parents = [i for i in range(M)]


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


for n in map(int, input().split()):
    idx = bisect_right(arr, n)
    idx = find(idx)
    answer.append(arr[idx])
    parents[idx] = idx + 1
print(*answer,sep='\n')
