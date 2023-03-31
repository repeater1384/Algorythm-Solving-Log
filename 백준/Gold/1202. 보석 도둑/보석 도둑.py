import sys
import heapq
from bisect import bisect_left

input = sys.stdin.readline
N, K = map(int, input().split())

jewels = []
bags = []
for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(jewels, (-v, m))

bags = [int(input()) for _ in range(K)]
parents = [i for i in range(K + 1)]


def find(x):
    # global parents
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[x] = y
    else:
        parents[y] = x


answer = 0
bags.sort()
while jewels:
    v, m = heapq.heappop(jewels)
    idx = bisect_left(bags, m)
    find_idx = find(idx)
    if find_idx == K:
        continue
    union(find_idx, find_idx + 1)
    answer -= v
print(answer)
