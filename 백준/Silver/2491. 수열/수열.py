N = int(input())
arr = [*map(int, input().split())]
answer = 1
continuous = 1
idx = 1
while idx < N:
    if arr[idx - 1] <= arr[idx]:
        continuous += 1
    else:
        answer = max(answer, continuous)
        continuous = 1
    idx += 1
answer = max(answer,continuous)

continuous = 1
idx = 1
while idx < N:
    if arr[idx - 1] >= arr[idx]:
        continuous += 1
    else:
        answer = max(answer, continuous)
        continuous = 1
    idx += 1
answer = max(answer,continuous)
print(answer)