import sys
import heapq

input = sys.stdin.readline
min_heap = []
max_heap = []

for i in range(int(input())):
    num = int(input())

    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))

    if i and min_heap[0][1] < max_heap[0][1]:
        min_temp, max_temp = heapq.heappop(min_heap)[1], heapq.heappop(max_heap)[1]
        heapq.heappush(min_heap, (max_temp, max_temp))
        heapq.heappush(max_heap, (-min_temp, min_temp))


    print(max_heap[0][1])

