N = int(input())
arr = list(map(int, input().split()))

answer = []
answer.append(arr[0])

for i in range(1, N):
    temp = sum(answer)
    answer.append(arr[i] * (i + 1) - temp)

for x in answer:
    print(x, end=' ')