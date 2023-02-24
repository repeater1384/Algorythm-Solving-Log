N, M = map(int, input().split())
arr = [0] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a:b + 1] = [c] * (b - a + 1)
print(*arr[1:])
