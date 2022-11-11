import heapq
import sys
input=sys.stdin.readline

N = int(input())
lines = [sorted(map(int, input().split())) for _ in range(N)]
lines.sort(key=lambda x: x[1])
D = int(input())

heap = []
answer = 0
for line in lines:
    if line[1] - line[0] > D:
        continue
    while heap and heap[0][0] < line[1] - D:
        heapq.heappop(heap)
    heapq.heappush(heap, line)
    answer = max(answer, len(heap))
print(answer)
