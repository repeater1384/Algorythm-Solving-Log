import heapq, sys

input = sys.stdin.readline

N, E = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

A, B = map(int, input().split())


def dijkstra(start):
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


# 1 -> ( A, B ) -> N
# 1 -> A -> B -> N
# 1 -> B -> A -> N
start1 = dijkstra(1)
startA = dijkstra(A)
startB = dijkstra(B)
answer = min(start1[A] + startA[B] + startB[N], start1[B] + startB[A] + startA[N])
print(-1 if answer == float('inf') else answer)
