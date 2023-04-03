from collections import deque

N = int(input())
K = int(input())
matrix = [[0] * N for _ in range(N)]

for _ in range(K):
    apple_y, apple_x = map(lambda x:int(x)-1, input().split())
    matrix[apple_y][apple_x] = 'a'

L = int(input())

dir_data = {}
for _ in range(L):
    X, C = input().split()
    dir_data[int(X)+1] = C

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 우, 하, 좌, 상
cur_dir_idx = 0

queue = deque([(0, 0)])
time = 0
while True:
    time += 1

    if time in dir_data.keys():
        C = dir_data[time]
        if C == 'D':
            cur_dir_idx += 1
        elif C == 'L':
            cur_dir_idx -= 1

    hx, hy = queue[0]
    dx, dy = dir[cur_dir_idx % 4]
    nx, ny = hx + dx, hy + dy

    if 0 <= nx < N and 0 <= ny < N:

        if matrix[ny][nx] == 'a':
            queue.appendleft((nx, ny))
            matrix[ny][nx] = 0
        elif (nx, ny) in queue:
            print(time)
            break
        else:
            queue.appendleft((nx, ny))
            queue.pop()

    else:
        print(time)
        break

