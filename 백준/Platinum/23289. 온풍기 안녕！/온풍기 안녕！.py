from collections import deque

N, M, K = map(int, input().split())
info_matrix = [[*map(int, input().split())] for _ in range(N)]

heater_list = []
check_list = []
for i in range(N):
    for j in range(M):
        if info_matrix[i][j] == 0:
            continue
        if info_matrix[i][j] == 5:
            check_list.append((i, j))
            continue
        heater_list.append((i, j, info_matrix[i][j]))

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
di, dj = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
ddir = [None, RIGHT, LEFT, UP, DOWN]
walls = [[[False] * 4 for _ in range(M)] for _ in range(N)]
W = int(input())
for _ in range(W):
    y, x, t = map(int, input().split())
    y -= 1
    x -= 1
    if t == 0:
        walls[y][x][UP] = True
        walls[y - 1][x][DOWN] = True
    elif t == 1:
        walls[y][x][RIGHT] = True
        walls[y][x + 1][LEFT] = True


def get_wind_spread_list(dir):
    # 우
    wind_spread_list = []
    if dir == 1:
        wind_spread_list.append((0, 1, [(0, 0, RIGHT)]))
        wind_spread_list.append((-1, 1, [(0, 0, UP), (-1, 0, RIGHT)]))
        wind_spread_list.append((1, 1, [(0, 0, DOWN), (1, 0, RIGHT)]))
    # 왼
    if dir == 2:
        wind_spread_list.append((0, -1, [(0, 0, LEFT)]))
        wind_spread_list.append((-1, -1, [(0, 0, UP), (-1, 0, LEFT)]))
        wind_spread_list.append((1, -1, [(0, 0, DOWN), (1, 0, LEFT)]))
    # 위
    if dir == 3:
        wind_spread_list.append((-1, 0, [(0, 0, UP)]))
        wind_spread_list.append((-1, -1, [(0, 0, LEFT), (0, -1, UP)]))
        wind_spread_list.append((-1, 1, [(0, 0, RIGHT), (0, 1, UP)]))
    # 아래
    if dir == 4:
        wind_spread_list.append((1, 0, [(0, 0, DOWN)]))
        wind_spread_list.append((1, -1, [(0, 0, LEFT), (0, -1, DOWN)]))
        wind_spread_list.append((1, 1, [(0, 0, RIGHT), (0, 1, DOWN)]))
    return wind_spread_list


# 온풍기들에서 바람이 나올때 늘어나는 온도를 저장한 배열.
# 벽이랑 온풍기의 위치는 변하지 않으므로 한번만 계산해주자.
add_temperature_matrix = [[0] * M for _ in range(N)]
for i, j, dir in heater_list:
    queue = deque()
    queue.append((i + di[dir], j + dj[dir], 5))
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True
    wind_spread_list = get_wind_spread_list(dir)

    while queue:
        ci, cj, add = queue.popleft()
        add_temperature_matrix[ci][cj] += add
        for di2, dj2, checks in wind_spread_list:
            ni, nj = ci + di2, cj + dj2
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                can_spread = True
                for di3, dj3, dir2 in checks:
                    if walls[ci + di3][cj + dj3][dir2]:
                        can_spread = False
                        break
                if can_spread and add > 1:
                    queue.append((ni, nj, add - 1))
                    visited[ni][nj] = True


def start_wind():
    global matrix
    for i in range(N):
        for j in range(M):
            matrix[i][j] += add_temperature_matrix[i][j]


def control_temperature():
    global matrix
    next_matrix = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            next_matrix[i][j] += matrix[i][j]
            for k in range(1, 5):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M and not walls[i][j][ddir[k]]:
                    my, you = matrix[i][j], matrix[ni][nj]
                    if my > you:
                        move = abs(my - you) // 4
                        next_matrix[i][j] -= move
                        next_matrix[ni][nj] += move
    matrix = next_matrix


SIDES = set()
for i in range(N):
    SIDES.add((i, 0))
    SIDES.add((i, M - 1))
for j in range(M):
    SIDES.add((0, j))
    SIDES.add((N - 1, j))


def control_side_temperature():
    global matrix
    for i, j in SIDES:
        if matrix[i][j] == 0:
            continue
        matrix[i][j] -= 1


def check():
    for i, j in check_list:
        if matrix[i][j] < K:
            return False
    return True


chocolate = 0
matrix = [[0] * M for _ in range(N)]
answer = 101
while chocolate < 100:
    # 1. 바람이 한번 나옴
    start_wind()
    # 2. 온도가 조절됨
    control_temperature()
    # 3. 사이드 온도가 조절됨
    control_side_temperature()
    # 4. 초콜릿을 하나 먹음
    chocolate += 1
    # 5. 조사할 모든 칸의 온도를 검사
    if check():
        answer = chocolate
        break
print(answer)
