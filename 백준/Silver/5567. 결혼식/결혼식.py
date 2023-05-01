from collections import deque

n = int(input())
adj = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    adj[a][b] = True
    adj[b][a] = True

visited = [False] * (n + 1)

queue = deque()
queue.append((1, 0))
visited[1] = True

answer = 0
while queue:
    cur, depth = queue.popleft()
    # print(cur,depth)
    for i in range(1, n + 1):
        if adj[cur][i]:
            if not visited[i]:
                queue.append((i, depth + 1))
                visited[i] = True
                if depth < 2:
                    answer += 1
print(answer)
