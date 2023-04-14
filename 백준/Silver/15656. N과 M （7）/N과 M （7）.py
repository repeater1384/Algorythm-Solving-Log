import sys


def j_comb(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield str(arr[i])
        else:
            for next in j_comb(arr, n - 1):
                yield str(arr[i]) + ' ' + next


N, M = map(int, input().split())
arr = [*map(int, input().split())]
arr.sort()
for a in j_comb(arr, M):
    print(a)
