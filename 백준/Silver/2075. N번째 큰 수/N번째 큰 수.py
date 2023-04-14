import heapq

N = int(input())

heap = []

for idx in range(N):
    arr = [*map(int, input().split())]
    if idx == 0:
        for value in arr:
            heapq.heappush(heap, value)
    else:
        for value in arr:
            heapq.heappush(heap, value)
            heapq.heappop(heap)

print(heap[0])
