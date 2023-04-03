N, M = map(int, input().split())
arr = [i for i in range(N + 1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    arr[i:j + 1] = arr[k:j + 1] + arr[i:k]
print(*arr[1:])
