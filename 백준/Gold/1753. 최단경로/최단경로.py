import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
INF = float('INF')

graph = [[] for _ in range(V + 1)]
cost = [INF] * (V + 1)
heap = []


def dijkstra(start):
    cost[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        cur_wei,now = heapq.heappop(heap)

        if cost[now] < cur_wei: continue

        for wei,next in graph[now]:
            next_wei = wei + cur_wei
            if next_wei < cost[next]:
                cost[next] = next_wei
                heapq.heappush(heap, (next_wei,next))


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))

dijkstra(K)


for i in range(1, V + 1):
    print("INF" if cost[i] == INF else cost[i])
