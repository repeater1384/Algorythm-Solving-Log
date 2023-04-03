import sys
from collections import deque

n = int(input())
if n == 1:
    print(0)
    sys.exit(0)
    
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))


def get_farthest_node(start):
    max_dist = 0
    max_node = None

    queue = deque([(start, 0)])
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        cur, dist = queue.popleft()
        for next, weight in graph[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append([next, dist + weight])
                if max_dist < dist + weight:
                    max_dist = dist + weight
                    max_node = next
    return max_node, max_dist


farthest_node, _ = get_farthest_node(1)
_, answer = get_farthest_node(farthest_node)

print(answer)
