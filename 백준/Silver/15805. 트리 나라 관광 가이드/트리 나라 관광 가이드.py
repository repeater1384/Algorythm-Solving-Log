N = int(input())
arr = [*map(int, input().split())]
parents = [-1] * N
cnt = 0
root = arr[0]
for i in range(1, N):
    a, b = arr[i - 1], arr[i]
    if parents[b] == -1:
        parents[b] = a
    cnt = max(cnt, b)
parents[root] = -1

print(cnt + 1)
print(*parents[:cnt + 1])
