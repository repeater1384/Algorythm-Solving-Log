from collections import deque

N, K = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
S, Y, X = map(int, input().split())

virusQueueList = [deque() for _ in range(K + 1)]
for i in range(N):
    for j in range(N):
        cur = matrix[i][j]
        if cur == 0:
            continue
        virusQueueList[cur].append((i, j))

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
# S초 동안 증식.
for _ in range(S):
    for k in range(1, K + 1):
        curQueue = virusQueueList[k]
        tempQueue = deque()
        while curQueue:
            y, x = curQueue.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if matrix[ny][nx] == 0:
                        tempQueue.append((ny, nx))
                        matrix[ny][nx] = k
        virusQueueList[k] = tempQueue

print(matrix[Y - 1][X - 1])
