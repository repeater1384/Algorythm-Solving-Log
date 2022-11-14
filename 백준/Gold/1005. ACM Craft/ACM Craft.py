import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())

    cost = [0] + [*map(int, input().split())]
    graph = [[] * (N + 1) for _ in range(N + 1)]
    inDegree = [0] * (N + 1)
    dp = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1

    target = int(input())
    queue = deque()

    for i in range(1, N + 1):
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] = cost[i]

    while queue:
        cur = queue.popleft()

        for i in graph[cur]:
            dp[i] = max(dp[i], dp[cur] + cost[i])
            
            inDegree[i] -= 1
            if inDegree[i] == 0:
                queue.append(i)

    print(dp[target])


for _ in range(int(input())):
    solution()
