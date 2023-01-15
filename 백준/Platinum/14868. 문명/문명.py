import sys
input = sys.stdin.readline


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


N, K = map(int, input().split())
matrix = [[-1] * N for _ in range(N)]
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
for i in range(K):
    x, y = map(lambda a: int(a) - 1, input().split())
    matrix[y][x] = i
visited = [[False] * N for _ in range(N)]
city = []
parents = [i for i in range(K)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] >= 0:
            visited[i][j] = True
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if matrix[ny][nx] >= 0:
                        union(matrix[i][j], matrix[ny][nx])
                    visited[ny][nx] = True
                    city.append((ny, nx))


def is_all_city_connected():
    for p in parents:
        if find(p) != 0:
            return False
    return True


answer = 0
while True:
    if is_all_city_connected():
        print(answer)
        break
    next_city = []
    while city:
        cy, cx = city.pop()
        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and matrix[ny][nx] == -1:
                    next_city.append((ny, nx))
                    visited[ny][nx] = True
                elif matrix[ny][nx] >= 0:
                    if matrix[cy][cx] == -1:
                        matrix[cy][cx] = matrix[ny][nx]
                    else:
                        union(matrix[cy][cx], matrix[ny][nx])
    city = next_city
    answer += 1
