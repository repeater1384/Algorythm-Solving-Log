N, K = map(int, input().split())

arr = [*map(int, input().split())]

answer = 0
use = set()
for i in range(len(arr)):
    if arr[i] in use:
        continue

    if len(use) < N:
        use.add(arr[i])
        continue

    next_find = []
    for u in use:
        try:
            find = arr.index(u, i)
        except ValueError:
            find = float('inf')
        next_find.append((u, find))

    next_find.sort(key=lambda x: -x[1])
    use.remove(next_find[0][0])
    use.add(arr[i])
    answer += 1

print(answer)
