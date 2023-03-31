N = int(input())
arr = [*map(int, input().split())]
idx = N - 1

while idx > 0:
    if sorted(arr[idx:])[::-1] != arr[idx:]:
        break
    idx -= 1

target = min(t for t in arr[idx + 1:] + [10001] if arr[idx] < t)
if target != 10001:
    t_idx = arr.index(target)
    arr[idx], arr[t_idx] = arr[t_idx], arr[idx]
    arr = arr[:idx + 1] + sorted(arr[idx + 1:])
    print(*arr)
else:
    print(-1)
