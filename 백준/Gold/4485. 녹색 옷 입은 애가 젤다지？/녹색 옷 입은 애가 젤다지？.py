import heapq
import sys

input = sys.stdin.readline

def dijkstra():
    cost = [[float('inf')] * N for _ in range(N)]
    cost[0][0] = matrix[0][0]
    heap = [(cost[0][0], 0, 0)]
    while heap:
        cur_cost, ci, cj = heapq.heappop(heap)
        if cur_cost < cost[ci][cj]:
            continue
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                next_cost = cur_cost + matrix[ni][nj]
                if next_cost < cost[ni][nj]:
                    cost[ni][nj] = next_cost
                    heapq.heappush(heap, (next_cost, ni, nj))

    return cost


di, dj = [-1, 1, 0, 0], [0, 0, 1, -1]
no = 1
while True:
    N = int(input())
    if N == 0:
        break

    matrix = [[*map(int, input().split())] for _ in range(N)]
    cost = dijkstra()
    print(f'Problem {no}: {cost[N - 1][N - 1]}')
    no += 1
