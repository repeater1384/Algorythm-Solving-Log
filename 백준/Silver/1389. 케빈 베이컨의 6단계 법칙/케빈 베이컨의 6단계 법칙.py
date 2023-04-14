from collections import deque
n,m = map(int,input().split())
graph = {idx:[]for idx in range(1,n+1)}
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


result = []
for idx in range(1,n+1):
    queue = deque()
    queue.append((idx,0))
    visited = [0] * (n+1)
    dis_res = 0
    while queue:
        cur,dis = queue.popleft()
        if visited[cur] == 0:
            dis_res += dis
            visited[cur] = 1
            for neighbor in graph[cur]:
                queue.append((neighbor,dis+1))

    result.append((dis_res,idx))

print(min(result)[1])
