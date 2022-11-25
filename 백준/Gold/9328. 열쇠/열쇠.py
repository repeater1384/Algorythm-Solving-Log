from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [['.'] * (M + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        matrix[i][1:M + 1] = [*input().strip()]
    temp = input().strip()
    keys = set() if temp == '0' else set(temp)

    queue = deque()
    visited = [[False] * (M + 2) for _ in range(N + 2)]
    answer = 0

    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        cy, cx = queue.popleft()
        if matrix[cy][cx] == '$':
            answer += 1
            matrix[cy][cx] = '.'
        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < N + 2 and 0 <= nx < M + 2 and not visited[ny][nx]:
                if 'A' <= matrix[ny][nx] <= 'Z':
                    # 문 따고 들어갈수 있을때
                    if matrix[ny][nx].lower() in keys:
                        visited[ny][nx] = True
                        queue.append((ny, nx))
                        matrix[ny][nx] = '.'

                if matrix[ny][nx] == '.' or matrix[ny][nx] == '$':
                    visited[ny][nx] = True
                    queue.append((ny, nx))

                # 키 먹었을때
                if 'a' <= matrix[ny][nx] <= 'z':
                    # 새로운 키인경우
                    if matrix[ny][nx] not in keys:
                        keys.add(matrix[ny][nx])
                        visited = [[False] * (M + 2) for _ in range(N + 2)]

                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    matrix[ny][nx] = '.'
    print(answer)
