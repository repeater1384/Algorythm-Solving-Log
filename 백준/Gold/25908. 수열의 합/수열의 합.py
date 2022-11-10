S, T = map(int, input().split())

arr = [0] * (T + 1)

for i in range(1, T + 1):
    isEven = i % 2 == 0
    for j in range(i, T + 1, i):
        arr[j] += 1 if isEven else -1

answer = sum(arr[S:T + 1])
print(answer)
