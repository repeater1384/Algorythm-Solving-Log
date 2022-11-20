from collections import deque

N, M = map(int, input().split())

matrix = [[*input()] for _ in range(N)]
# visited[i][j][key] i,j 지점에 key를 들고 방문한 시간
visited = [[[float('inf')] * M for _ in range(N)] for _ in range(64)]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == '0':
            matrix[i][j] = '.'
            si = i
            sj = j
            break

# visited에 내가 먹은 열쇠들을 비트마스킹으로 기록해놓고 움직임
# 이미 방문했더라도 새로운 열쇠를 먹고 방문하는건 가능해야함
queue = deque()
queue.append((si, sj, 0, 0))
visited[0][si][sj] = 0

di, dj = [0, 0, 1, -1], [1, -1, 0, 0]
answer = -1
while queue:
    ci, cj, cnt, eat_key = queue.popleft()
    if matrix[ci][cj] == '1':
        answer = cnt
        break

    for k in range(4):
        ni = ci + di[k]
        nj = cj + dj[k]
        next_eat_key = eat_key
        if 0 <= ni < N and 0 <= nj < M:
            if visited[eat_key][ni][nj] <= cnt + 1 or matrix[ni][nj] == '#':
                continue

            if 'A' <= matrix[ni][nj] <= 'F':
                if eat_key & (1 << ord(matrix[ni][nj]) - ord('A')) == 0:
                    continue

            if 'a' <= matrix[ni][nj] <= 'f':
                next_eat_key |= (1 << ord(matrix[ni][nj]) - ord('a'))

            visited[next_eat_key][ni][nj] = cnt + 1
            queue.append((ni, nj, cnt + 1, next_eat_key))

print(answer)
