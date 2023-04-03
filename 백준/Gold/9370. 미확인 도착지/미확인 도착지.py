import queue
import sys

input = sys.stdin.readline


def dijkstra(start, n, adjList):
    weight = [10 ** 7] * (n + 1)
    pq = queue.PriorityQueue()
    pq.put((0, start))
    weight[start] = 0
    while not pq.empty():
        cur = pq.get()

        if weight[cur[1]] < cur[0]:
            continue

        for next in adjList[cur[1]]:
            cost = cur[0] + next[1]
            if cost < weight[next[0]]:
                weight[next[0]] = cost
                pq.put((cost, next[0]))

    return weight


for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    adjList = [[] for _ in range(n + 1)]

    # g랑 h를 잇는길
    path4 = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            path4 = d
        adjList[a].append((b, d))
        adjList[b].append((a, d))

    hubos = [int(input()) for _ in range(t)]

    # start에서 시작해서 후보들로 바로 가는 리스트
    path1 = dijkstra(s, n, adjList)

    # g에서 시작
    path2 = dijkstra(g, n, adjList)

    # h에서 시작
    path3 = dijkstra(h, n, adjList)

    answer = []
    for hubo in hubos:
        route1 = path1[hubo]
        # start -> h -> g -> hubo
        route2 = path1[h] + path4 + path2[hubo]
        # start -> g -> h -> hubo
        route3 = path1[g] + path4 + path3[hubo]
        if route1 == route2 or route1 == route3:
            answer.append(hubo)

    print(*sorted(answer))
