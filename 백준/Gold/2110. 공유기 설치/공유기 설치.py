import sys

N, C = map(int, input().split())
arr = sorted([int(sys.stdin.readline()) for _ in range(N)])

start, end = 1, max(arr)-min(arr)

answer = 0
while start <= end:
    mid = (start + end) // 2

    count = 1
    cur_house = arr[0]
    for i in range(1, N):
        if arr[i] - cur_house >= mid:
            count += 1
            cur_house = arr[i]

    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
