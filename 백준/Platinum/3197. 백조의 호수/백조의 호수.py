import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())

matrix = [[*input()] for _ in range(R)]

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
swans = []

for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'L':
            swans.append([i, j])
            matrix[i][j] = '.'

ice = []
p_num = 0
visited = [[False] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if matrix[i][j] == '.' and not visited[i][j]:
            queue = deque()
            queue.append((i, j))
            while queue:
                cy, cx = queue.popleft()
                matrix[cy][cx] = p_num
                visited[cy][cx] = True
                for k in range(4):
                    ny, nx = cy + dy[k], cx + dx[k]
                    if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                        if matrix[ny][nx] == '.':
                            queue.append((ny, nx))
                        if matrix[ny][nx] == 'X':
                            ice.append((ny, nx))
                        visited[ny][nx] = True
            p_num += 1

parents = [i for i in range(p_num)]


def find(x):
    global parents
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    global parents
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

answer = 0
while find(matrix[swans[0][0]][swans[0][1]]) != find(matrix[swans[1][0]][swans[1][1]]):
    temp_ice = []
    while ice:
        cy, cx = ice.pop()
        visited[cy][cx] = True
        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < R and 0 <= nx < C:
                if matrix[ny][nx] == 'X':
                    if not visited[ny][nx]:
                        temp_ice.append((ny, nx))
                        visited[ny][nx] = True
                else:
                    if matrix[cy][cx] == 'X':
                        matrix[cy][cx] = matrix[ny][nx]
                    else:
                        union(matrix[cy][cx], matrix[ny][nx])

    ice = temp_ice
    answer += 1

print(answer)