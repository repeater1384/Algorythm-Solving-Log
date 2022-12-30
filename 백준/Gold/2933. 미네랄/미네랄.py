from collections import deque


def is_in_air(i, j):
    # i,j가 포함된 블럭이 공중에 떠 있나요?
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    visited[i][j] = True
    queue.append((i, j))
    while queue:
        y, x = queue.popleft()
        if y == N - 1:
            return False
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and matrix[ny][nx] == 'x':
                queue.append((ny, nx))
                visited[ny][nx] = True
    return True


def fall_cluster(i, j):
    # i,j를 포함한 블럭을 떨어뜨립니다.
    bottom = {}
    all_block = []
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    visited[i][j] = True
    queue.append((i, j))
    while queue:
        y, x = queue.popleft()
        bottom[x] = max(bottom.get(x, 0), y)
        all_block.append((y, x))
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and matrix[ny][nx] == 'x':
                queue.append((ny, nx))
                visited[ny][nx] = True

    for c, r in bottom.items():
        for nr in range(r + 1, N):
            if matrix[nr][c] == 'x':
                bottom[c] = nr - 1 - r
                break
        else:
            bottom[c] = N - 1 - r
    fall = min(bottom.values())
    for y, x in all_block:
        matrix[y][x] = '.'
    for y, x in all_block:
        matrix[y + fall][x] = 'x'


N, M = map(int, input().split())
matrix = [[*input()] for _ in range(N)]
input()

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
for i, height in enumerate(map(lambda x: N - int(x), input().split())):
    if i % 2 == 0:
        col = range(M)
    else:
        col = range(M - 1, -1, -1)

    for c in col:
        if matrix[height][c] == 'x':
            matrix[height][c] = '.'
            for k in range(4):
                ny, nx = height + dy[k], c + dx[k]
                if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 'x':
                    if is_in_air(ny, nx):
                        fall_cluster(ny, nx)
            break

print(*(''.join(row) for row in matrix), sep='\n')
