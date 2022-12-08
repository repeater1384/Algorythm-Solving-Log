import heapq, sys

input = sys.stdin.readline

N = int(input())
M = int(input())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))

S, E = map(int, input().split())


def dijkstra_with_trace(start, end):
    # 최소비용과 경로를 담은 리스트 리턴

    cost = [float('inf')] * (N + 1)
    parents = [-1] * (N + 1)
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
                parents[next_node] = cur_node
    trace = [end]
    cur = end
    while parents[cur] != -1:
        cur = parents[cur]
        trace.append(cur)
    return cost[end], trace[::-1]


min_cost, trace = dijkstra_with_trace(S, E)
print(min_cost)
print(len(trace))
print(*trace)
