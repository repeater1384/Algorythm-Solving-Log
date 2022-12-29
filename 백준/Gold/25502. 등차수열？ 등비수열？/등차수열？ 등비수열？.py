import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [*map(int, input().split())]
diff_dict, rate_dict = {}, {}
for i in range(N - 1):
    diff = arr[i + 1] - arr[i]
    rate = arr[i + 1] / arr[i]
    diff_dict[diff] = diff_dict.get(diff, 0) + 1
    rate_dict[rate] = rate_dict.get(rate, 0) + 1

answer = []
for _ in range(M):
    i, v = map(int, input().split())
    for j in range(i - 1, i + 1):
        if 0 < j < N:
            diff = arr[j] - arr[j - 1]
            rate = arr[j] / arr[j - 1]
            if diff_dict[diff] == 1:
                diff_dict.pop(diff)
            else:
                diff_dict[diff] -= 1
            if rate_dict[rate] == 1:
                rate_dict.pop(rate)
            else:
                rate_dict[rate] -= 1
    arr[i - 1] = v
    for j in range(i - 1, i + 1):
        if 0 < j < N:
            diff = arr[j] - arr[j - 1]
            rate = arr[j] / arr[j - 1]
            diff_dict[diff] = diff_dict.get(diff, 0) + 1
            rate_dict[rate] = rate_dict.get(rate, 0) + 1

    if len(diff_dict.keys()) == 1 and arr[1] > arr[0]:
        answer.append('+')
    elif len(rate_dict.keys()) == 1 and arr[1] % arr[0] == 0:
        answer.append('*')
    else:
        answer.append('?')

print('\n'.join(answer))
