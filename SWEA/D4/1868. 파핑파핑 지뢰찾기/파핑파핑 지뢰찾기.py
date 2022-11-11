from collections import deque

dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]
T = int(input())
for t in range(T):
    N = int(input())
    matrix = [[*input()] for _ in range(N)]
    numbered_matrix = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if matrix[y][x] != '*':
                continue
            numbered_matrix[y][x] = -1
            visited[y][x] = True
            for k in range(8):
                ny, nx = y + dy[k], x + dx[k]
                if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == '.':
                    numbered_matrix[ny][nx] += 1

    answer = 0
    # 1. 0인거 클릭해서 한번에 많이많이 지우기
    for y in range(N):
        for x in range(N):
            if numbered_matrix[y][x] != 0 or visited[y][x]:
                continue
            answer += 1
            queue = deque()
            queue.append((y, x))
            visited[y][x] = True
            while queue:
                cy, cx = queue.popleft()
                for k in range(8):
                    ny, nx = cy + dy[k], cx + dx[k]
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                        if numbered_matrix[ny][nx] == 0:
                            queue.append((ny, nx))
                        visited[ny][nx] = True
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                answer += 1
    print('#'+str(t+1),answer)
