import heapq

N, K = map(int, input().split())
arr = [*map(int, input().split())]


def solve(iterable, _K):
    h = []

    for value in iterable:
        heapq.heappush(h, value)

    for _ in range(_K - 1):
        heapq.heappop(h)

    return heapq.heappop(h)


print(solve(arr, K))
