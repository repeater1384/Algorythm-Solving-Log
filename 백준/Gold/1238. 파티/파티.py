import heapq

N, M, X = map(int, input().split())
adj_list1 = [[] for _ in range(N + 1)]
adj_list2 = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list1[a].append((b, c))
    adj_list2[b].append((a, c))


def dijkstra(adj_list, start):
    cost = [float('inf')] * (N + 1)
    pq = []
    cost[start] = 0
    heapq.heappush(pq, (cost[start], start))
    while pq:
        cur_dis, cur_node = heapq.heappop(pq)
        if cost[cur_node] < cur_dis:
            continue
        for next_node, next_dis in adj_list[cur_node]:
            if cost[next_node] > cur_dis + next_dis:
                cost[next_node] = cur_dis + next_dis
                heapq.heappush(pq, (cur_dis + next_dis, next_node))
    return cost


dis1 = dijkstra(adj_list1, X)
dis2 = dijkstra(adj_list2, X)
print(max(dis1[i] + dis2[i] for i in range(1, N + 1)))
