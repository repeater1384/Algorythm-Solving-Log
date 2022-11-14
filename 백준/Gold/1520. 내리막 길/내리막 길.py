import heapq

N, M = map(int, input().split())
matrix = [[*map(lambda n: -int(n), input().split())] for _ in range(N)]
path = [[0] * M for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
heap = [(matrix[0][0], 0, 0)]
path[0][0] = 1
while heap:
    height, y, x = heapq.heappop(heap)
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < N and 0 <= nx < M and matrix[y][x] < matrix[ny][nx]:
            if path[ny][nx] == 0:
                heapq.heappush(heap, (matrix[ny][nx], ny, nx))
            path[ny][nx] += path[y][x]
print(path[N - 1][M - 1])
