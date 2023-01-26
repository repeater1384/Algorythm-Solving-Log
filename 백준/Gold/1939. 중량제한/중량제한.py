import sys
from collections import deque

input = sys.stdin.readline


def bfs(weight):
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        cur = queue.popleft()
        if cur == end:
            return True
        for k, v in adj_list[cur].items():
            if weight <= v and not visited[k]:
                queue.append(k)
                visited[k] = True
    return False


N, M = map(int, input().split())

adj_list = [{} for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a][b] = max(adj_list[a].get(b, 0), c)
    adj_list[b][a] = max(adj_list[b].get(a, 0), c)

start, end = map(int, input().split())
s, e = 1, 1_000_000_000
while s <= e:
    m = (s + e) // 2
    if bfs(m):
        s = m + 1
    else:
        e = m - 1
print(e)
