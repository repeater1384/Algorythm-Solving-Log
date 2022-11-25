from collections import deque
import sys

input = sys.stdin.readline

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
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
    queue.append((0, 0))
    visited[0][0] = True

    answer = 0
    while queue:
        cy, cx = queue.popleft()
        if matrix[cy][cx] == '$':
            answer += 1
            matrix[cy][cx] = '.'

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < N + 2 and 0 <= nx < M + 2 and matrix[ny][nx] != '*' and not visited[ny][nx]:
                if 'A' <= matrix[ny][nx] <= 'Z' and matrix[ny][nx].lower() not in keys:
                    continue
                # 처음 먹는 키
                if 'a' <= matrix[ny][nx] <= 'z' and matrix[ny][nx] not in keys:
                    keys.add(matrix[ny][nx])
                    visited = [[False] * (M + 2) for _ in range(N + 2)]

                visited[ny][nx] = True
                queue.append((ny, nx))

    print(answer)
