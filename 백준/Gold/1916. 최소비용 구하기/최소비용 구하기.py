import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
cost = [INF] * (N + 1)
heap = []


def dijkstra(start):
    cost[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        wei, cur = heapq.heappop(heap)
        
        if cost[cur] < wei:continue
        
        for w, next in graph[cur]:
            next_wei = w + wei
            if cost[next] > next_wei:
                cost[next] = next_wei
                heapq.heappush(heap, (next_wei, next))


for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

start, end = map(int, input().split())

dijkstra(start)

print(cost[end])
