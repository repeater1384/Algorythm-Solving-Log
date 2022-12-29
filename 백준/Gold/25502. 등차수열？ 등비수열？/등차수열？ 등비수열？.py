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

for _ in range(M):
    i, v = map(int, input().split())
    i -= 1
    if i != 0:
        diff = arr[i] - arr[i - 1]
        rate = arr[i] / arr[i - 1]
        if diff_dict[diff] == 1:
            diff_dict.pop(diff)
        else:
            diff_dict[diff] -= 1
        if rate_dict[rate] == 1:
            rate_dict.pop(rate)
        else:
            rate_dict[rate] -= 1

    if i != N - 1:
        diff = arr[i + 1] - arr[i]
        rate = arr[i + 1] / arr[i]
        if diff_dict[diff] == 1:
            diff_dict.pop(diff)
        else:
            diff_dict[diff] -= 1
        if rate_dict[rate] == 1:
            rate_dict.pop(rate)
        else:
            rate_dict[rate] -= 1

    arr[i] = v

    if i != 0:
        diff = arr[i] - arr[i - 1]
        rate = arr[i] / arr[i - 1]
        diff_dict[diff] = diff_dict.get(diff, 0) + 1
        rate_dict[rate] = rate_dict.get(rate, 0) + 1
    if i != N - 1:
        diff = arr[i + 1] - arr[i]
        rate = arr[i + 1] / arr[i]
        diff_dict[diff] = diff_dict.get(diff, 0) + 1
        rate_dict[rate] = rate_dict.get(rate, 0) + 1

    if len(diff_dict.keys()) == 1 and [*diff_dict.keys()][0] > 0:
        print('+')
    elif len(rate_dict.keys()) == 1 and 0 < [*rate_dict.keys()][0] == int([*rate_dict.keys()][0]):
        print('*')
    else:
        print('?')
