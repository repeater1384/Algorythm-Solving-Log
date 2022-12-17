N, K = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    if arr[i][0] == K:
        arr[i][0] = -1
arr.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))

for i in range(N):
    if arr[i][0] == -1:
        print(i + 1)
