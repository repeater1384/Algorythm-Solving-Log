from collections import deque


def bfs(_x, _y, _endx, _endy, _size):
    global visited

    queue = deque()
    queue.append((_x, _y, 0))
    dx, dy = [1, 2, 2, 1, -1, -2, -2, -1], [-2, -1, 1, 2, 2, 1, -1, -2]
    visited[_y][_x] = True
    while queue:
        cx, cy, dis = queue.popleft()
        # print(cx, cy, dis)

        if cx == _endx and cy == _endy:
            return dis

        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < _size and 0 <= ny < _size and not visited[ny][nx]:
                queue.append((nx, ny, dis + 1))
                visited[ny][nx] = True


for _ in range(int(input())):
    size = int(input())
    visited = [[False] * size for _ in range(size)]
    x, y = map(int, input().split())
    endx, endy = map(int, input().split())
    result = bfs(x, y, endx, endy, size)
    print(result)
    
# from collections import deque
#
#
# def bfs(_x, _y, _endx, _endy, _size):
#     global visited
#
#     queue = deque()
#     queue.append((_x, _y, 0))
#     dx, dy = [1, 2, 2, 1, -1, -2, -2, -1], [-2, -1, 1, 2, 2, 1, -1, -2]
#
#     while queue:
#         cx, cy, dis = queue.popleft()
#         visited[cy][cx] = True
#
#         if cx == _endx and cy == _endy:
#             return dis
#
#         for i in range(8):
#             nx, ny = cx + dx[i], cy + dy[i]
#             if 0 <= nx < _size and 0 <= ny < _size and not visited[ny][nx]:
#                 queue.append((nx, ny, dis + 1))
#
#
# for _ in range(int(input())):
#     size = int(input())
#     visited = [[False] * size for _ in range(size)]
#     x, y = map(int, input().split())
#     endx, endy = map(int, input().split())
#     result = bfs(x, y, endx, endy, size)
#     print(result)