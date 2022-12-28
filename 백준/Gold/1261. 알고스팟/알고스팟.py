import heapq

M, N = map(int, input().split())
matrix = [[*map(int, input())] for _ in range(N)]

adj_list = [[] for _ in range(N * M)]
di, dj = [0, 0, 1, -1], [1, -1, 0, 0]
for i in range(N):
    for j in range(M):
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                adj_list[i * M + j].append((ni * M + nj, matrix[ni][nj]))
INF = float('inf')


def dijkstra(start):
    cost = [INF] * (N * M)
    heap = [(0, start)]
    cost[start] = 0
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        if cost[cur_node] < cur_cost:
            continue
        for next_node, next_cost in adj_list[cur_node]:
            total_cost = cur_cost + next_cost
            if cost[next_node] > total_cost:
                cost[next_node] = total_cost
                heapq.heappush(heap, (total_cost, next_node))
    return cost


final_cost = dijkstra(0)
print(final_cost[N * M - 1])
