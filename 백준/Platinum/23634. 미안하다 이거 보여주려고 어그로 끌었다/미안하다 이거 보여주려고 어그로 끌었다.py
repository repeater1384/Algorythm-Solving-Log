from collections import deque
import sys
sys.setrecursionlimit(200000)

N, M = map(int, input().split())
matrix = [[*map(int, input())] for _ in range(N)]
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]

rock_section = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
rock_section_num = 0
# 돌로 나뉘어진 구역을 표시합니다.
for i in range(N):
    for j in range(M):
        if not visited[i][j] and matrix[i][j] != 2:
            queue = deque()
            visited[i][j] = True
            queue.append((i, j))
            while queue:
                cy, cx = queue.popleft()
                rock_section[cy][cx] = rock_section_num
                for k in range(4):
                    ny, nx = cy + dy[k], cx + dx[k]
                    if 0 <= ny < N and 0 <= nx < M:
                        if not visited[ny][nx] and matrix[ny][nx] != 2:
                            queue.append((ny, nx))
                            visited[ny][nx] = True
            rock_section_num += 1

fire_section = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
rock_fire = {key: [] for key in range(rock_section_num)}
fire = []
fire_section_num = 0
# 불로 나뉘어진 구역을 표시합니다.
for i in range(N):
    for j in range(M):
        if not visited[i][j] and matrix[i][j] == 0:
            queue = deque()
            visited[i][j] = True
            queue.append((i, j))
            rock_fire[rock_section[i][j]].append(fire_section_num)
            while queue:
                cy, cx = queue.popleft()
                fire_section[cy][cx] = fire_section_num
                for k in range(4):
                    ny, nx = cy + dy[k], cx + dx[k]
                    if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                        visited[ny][nx] = True
                        if matrix[ny][nx] == 0:
                            queue.append((ny, nx))
                        if matrix[ny][nx] == 1:
                            fire.append((ny, nx))
            fire_section_num += 1

parents = [i for i in range(fire_section_num)]


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


# 불이 연결되어있는지 확인.
def is_all_fire_connected():
    # return len(set(map(lambda x: find(x), parents))) == rock_section_num

    for key, value in rock_fire.items():
        if not value:
            continue
        a = find(value[0])
        for i in range(1, len(value)):
            if find(value[i]) != a:
                return False
    return True


answer_day = 0
visited = [[False] * M for _ in range(N)]
while True:
    if is_all_fire_connected() or not fire:
        answer_size = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    answer_size += 1
        print(answer_day, answer_size)
        break
    temp_fire = []
    while fire:
        cy, cx = fire.pop()
        matrix[cy][cx] = 0
        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            # 방문 안한 나무를 만남
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and matrix[ny][nx] == 1:
                    temp_fire.append((ny, nx))
                    visited[ny][nx] = True
                elif fire_section[ny][nx] >= 0:
                    if fire_section[cy][cx] == -1:
                        fire_section[cy][cx] = fire_section[ny][nx]
                    else:
                        union(fire_section[cy][cx], fire_section[ny][nx])
            # if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            #     if matrix[ny][nx] == 2:
            #         continue
            #     if matrix[ny][nx] == 1:
            #         matrix[ny][nx] = 0
            #         visited[ny][nx] = True
            #         fire_section[ny][nx] = fire_section[cy][cx]
            #         temp_fire.append((ny, nx))
            #         for k2 in range(4):
            #             nny, nnx = ny + dy[k2], nx + dx[k2]
            #             if 0 <= nny < N and 0 <= nnx < M and matrix[nny][nnx] == 0 and fire_section[nny][nnx] != \
            #                     fire_section[ny][nx]:
            #                 union(fire_section[ny][nx], fire_section[nny][nnx])
            #     if matrix[ny][nx] == 0 and fire_section[cy][cx] != fire_section[ny][nx]:
            #         union(fire_section[cy][cx], fire_section[ny][nx])
    fire = temp_fire
    answer_day += 1
