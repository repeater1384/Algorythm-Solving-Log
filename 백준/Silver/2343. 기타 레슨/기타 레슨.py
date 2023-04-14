N, M = map(int, input().split())
arr = [*map(int, input().split())]

start, end = max(arr), sum(arr)

while start <= end:
    mid = (start + end) // 2

    cur_acc = 0
    count = 1
    for i in range(N):
        cur_acc += arr[i]
        if cur_acc > mid:
            count += 1
            cur_acc = arr[i]

    if count <= M:
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)
