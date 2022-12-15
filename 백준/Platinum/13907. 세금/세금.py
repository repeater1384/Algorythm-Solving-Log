import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

N, M, K = map(int, input().split())
S, D = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))
tax = [0]
for _ in range(K):
    tax.append(int(input()))


def dijkstra(start):
    _dist = [[INF] * N for _ in range(N + 1)]
    # 현재 까지 비용,  현재 까지 지나온 노드 수, 현재 정점
    pq = [(0, 0, start)]
    _dist[start][0] = 0
    while pq:
        cur_cost, cur_edge_cnt, cur_node = heapq.heappop(pq)
        flag = False
        for i in range(cur_edge_cnt):
            if _dist[cur_node][i] < cur_cost:
                flag = True
                break
        if _dist[cur_node][cur_edge_cnt] < cur_cost or cur_edge_cnt == N - 1 or flag:
            continue
        for next_node, next_cost in adj_list[cur_node]:
            final_cost = cur_cost + next_cost
            if _dist[next_node][cur_edge_cnt + 1] > final_cost:
                _dist[next_node][cur_edge_cnt + 1] = final_cost
                heapq.heappush(pq, (final_cost, cur_edge_cnt + 1, next_node))
    return _dist


dist = dijkstra(S)[D]

acc_tax = 0
answer = []
for t in tax:
    acc_tax += t
    min_cost = INF
    for idx, cost in enumerate(dist):
        min_cost = min(min_cost, cost + idx * acc_tax)
    answer.append(min_cost)
print(*answer, sep='\n')
