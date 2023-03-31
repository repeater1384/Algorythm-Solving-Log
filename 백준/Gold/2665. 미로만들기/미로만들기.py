import heapq

N = int(input())
matrix = [[*map(int, input())] for _ in range(N)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

visited = [[float('inf')] * N for _ in range(N)]
heap = []
visited[0][0] = 0
heapq.heappush(heap, (0, 0, 0))
answer = float('inf')
while heap:
    cnt, y, x = heapq.heappop(heap)
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if matrix[ny][nx] == 1 and visited[ny][nx] > cnt:
                visited[ny][nx] = cnt
                heapq.heappush(heap, (cnt, ny, nx))
            if matrix[ny][nx] == 0 and visited[ny][nx] > cnt + 1:
                visited[ny][nx] = cnt + 1
                heapq.heappush(heap, (cnt + 1, ny, nx))

print(visited[N - 1][N - 1])
