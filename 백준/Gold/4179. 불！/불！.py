import sys

input = sys.stdin.readline
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]

N, M = map(int, input().split())
matrix = [[*input().rstrip()] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
fire = []
human = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'F':
            fire.append((i, j))
        elif matrix[i][j] == 'J':
            matrix[i][j] = '.'
            visited[i][j] = True
            human.append((i, j))

answer = -1
cnt = 1
while human:
    if answer > 0:
        break
    next_fire = []
    for i, j in fire:
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == '.':
                next_fire.append((ni, nj))
                matrix[ni][nj] = 'F'

    next_human = []
    for i, j in human:
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni == -1 or ni == N or nj == -1 or nj == M:
                answer = cnt
            else:
                if matrix[ni][nj] == '.' and not visited[ni][nj]:
                    next_human.append((ni, nj))
                    visited[ni][nj] = True

    fire = next_fire
    human = next_human
    cnt += 1
print('IMPOSSIBLE' if answer == -1 else answer)
