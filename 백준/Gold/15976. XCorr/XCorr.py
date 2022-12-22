import sys, bisect

input = sys.stdin.readline

y_idx = []
y_val = []
target = {}
N = int(input())
for _ in range(N):
    idx, val = map(int, input().split())
    target[idx] = val
M = int(input())
for _ in range(M):
    idx, val = map(int, input().split())
    y_idx.append(idx)
    y_val.append(val)

A = int(input())
B = int(input())
y_prefix = [0]
for y in y_val:
    y_prefix.append(y_prefix[-1] + y)

answer = 0
for idx, val in target.items():
    low = bisect.bisect_left(y_idx, idx + A)
    high = bisect.bisect_left(y_idx, idx + B + 1)
    answer += val * (y_prefix[high] - y_prefix[low])
print(answer)
