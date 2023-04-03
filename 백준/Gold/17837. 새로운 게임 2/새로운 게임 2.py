import sys

N, K = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
board = [[[] for _ in range(N)] for _ in range(N)]
unit_pos = [[-1, -1] for _ in range(K)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

for n in range(K):
    y, x, d = map(lambda x: int(x) - 1, input().split())
    board[y][x].append([n, d])
    unit_pos[n] = [y, x]

for time in range(1, 1000):
    # 시뮬레이션
    for n in range(K):
        y, x = unit_pos[n]
        d, i = -1, -1
        for _i in range(len(board[y][x])):
            _n, _d = board[y][x][_i]
            if _n == n:
                d = _d
                i = _i
                break

        ny, nx = y + dy[d], x + dx[d]
        # blue / edge 체크
        if ny < 0 or N <= ny or nx < 0 or N <= nx or matrix[ny][nx] == 2:
            nd = (d + 1) % 2 if d < 2 else (d + 1) % 2 + 2
            board[y][x][i][1] = nd
            ny, nx = y + dy[nd], x + dx[nd]

        if ny < 0 or N <= ny or nx < 0 or N <= nx or matrix[ny][nx] == 2:
            continue
        elif matrix[ny][nx] == 0:
            for _n, _ in board[y][x][i:]:
                unit_pos[_n] = [ny, nx]
            board[ny][nx].extend(board[y][x][i:])
            if len(board[ny][nx]) >= 4:
                print(time)
                sys.exit(0)
            board[y][x] = board[y][x][:i]
        elif matrix[ny][nx] == 1:
            for _n, _ in board[y][x][i:]:
                unit_pos[_n] = [ny, nx]
            board[ny][nx].extend(board[y][x][i:][::-1])
            if len(board[ny][nx]) >= 4:
                print(time)
                sys.exit(0)
            board[y][x] = board[y][x][:i]


    # print(unit_pos)
    # print(*board, sep='\n')
    # print('-' * 50)
print(-1)
