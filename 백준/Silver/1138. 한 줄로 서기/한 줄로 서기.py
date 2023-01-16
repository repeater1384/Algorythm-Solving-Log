N = int(input())
arr = [*map(int, input().split())]

answer = []
for i in range(N - 1, -1, -1):
    cur = arr[i]
    answer.insert(cur, i + 1)

print(*answer)
