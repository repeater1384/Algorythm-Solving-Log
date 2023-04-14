import copy

N = int(input())

original_matrix = [[*input()] for _ in range(N)]

def bfs1(sx, sy, color, _matrix):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = [(sx, sy)]
    _matrix[sy][sx] = 0
    while queue:
        cx, cy = queue.pop(0)
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if _matrix[ny][nx] == color:
                    _matrix[ny][nx] = 0
                    queue.append((nx, ny))


def bfs2(sx, sy, color, _matrix):  # R==G

    if color == 'R' or color == 'G':
        color = ['R', 'G']
    else:
        color = ['B']

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = [(sx, sy)]
    _matrix[sy][sx] = 0
    while queue:
        cx, cy = queue.pop(0)
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if _matrix[ny][nx] in color:
                    _matrix[ny][nx] = 0
                    queue.append((nx, ny))


result1 = 0
copied_matrix = copy.deepcopy(original_matrix)
for y in range(N):
    for x in range(N):
        if copied_matrix[y][x] != 0:
            result1 += 1
            bfs1(x, y, copied_matrix[y][x], copied_matrix)


result2 = 0
copied_matrix = copy.deepcopy(original_matrix)
for y in range(N):
    for x in range(N):
        if copied_matrix[y][x] != 0:
            result2 += 1
            bfs2(x, y, copied_matrix[y][x], copied_matrix)


print(result1, result2)
