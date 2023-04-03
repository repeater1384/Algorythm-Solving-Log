import heapq
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)


def dijkstra(start):
    dis = [float('inf')] * (N + 1)
    dis[start] = 0
    heap = [(0, start)]

    while heap:
        cur_dis, cur_node = heapq.heappop(heap)
        if dis[cur_node] < cur_dis:
            continue
        for next_node in adj_list[cur_node]:
            if cur_dis + 1 < dis[next_node]:
                dis[next_node] = cur_dis + 1
                heapq.heappush(heap, (cur_dis + 1, next_node))

    return dis


distance = dijkstra(X)
answer = []
for i in range(1, N + 1):
    if distance[i] == K:
        answer.append(i)
print(*answer if answer else [-1], sep='\n')
