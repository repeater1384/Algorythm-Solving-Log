import sys

input = sys.stdin.readline


def round(n):
    return int(n) + 1 if n - int(n) >= 0.5 else int(n)


n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

k = round(n * 0.15)
new_arr = arr[k:len(arr) - k]
print(round(sum(new_arr) / len(new_arr)) if len(new_arr) > 0 else 0)
