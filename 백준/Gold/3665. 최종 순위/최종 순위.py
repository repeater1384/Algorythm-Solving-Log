import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n = int(input())
    rank = [*map(int, input().split())]
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    inDegree = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1, n):
            graph[rank[j]][rank[i]] = True
            inDegree[rank[i]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        if graph[a][b]:  # a가 b보다 순위가 낮았는데, 바뀌어서 높아진 경우.
            inDegree[a] += 1
            inDegree[b] -= 1
            graph[a][b] = False
            graph[b][a] = True
        else:
            inDegree[a] -= 1
            inDegree[b] += 1
            graph[a][b] = True
            graph[b][a] = False

    queue = deque()
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)

    answer = []
    while queue:
        cur = queue.popleft()
        answer.append(cur)

        for i in range(1, n + 1):
            if graph[cur][i]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    queue.append(i)

    if len(answer) == n:
        print(*answer[::-1])
    else:
        print("IMPOSSIBLE")


for _ in range(int(input())):
    solution()
