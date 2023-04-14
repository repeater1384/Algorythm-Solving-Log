import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]
inDegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

heap = []
result = []

for i in range(1, N + 1):
    if inDegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    cur = heapq.heappop(heap)
    result.append(cur)
    for i in graph[cur]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(heap, i)

print(*map(str, result))