from collections import deque

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
    
INF = float('inf')
distance = [INF] * (N + 1)

queue = deque()
queue.append((1, 0))
distance[1] = 0
while queue:
    cur, dis = queue.popleft()
    for next in adj_list[cur]:
        if distance[next] == INF:
            distance[next] = dis + 1
            queue.append((next, dis + 1))

max_dis = max(distance[1:])
count_max_dis = distance.count(max_dis)
node_max_dis = distance.index(max_dis)
print(node_max_dis, max_dis, count_max_dis)
