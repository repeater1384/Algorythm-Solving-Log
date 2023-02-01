from collections import deque

K = int(input())
M, N = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
di1, dj1 = [-2, -2, -1, 1, 2, 2, 1, -1], [-1, 1, 2, 2, 1, -1, -2, -2]
di2, dj2 = [-1, 1, 0, 0], [0, 0, 1, -1]

# 0,0 -> N-1, M-1
# visited[n][m][k] -> n,m위치에 k번 뛰어서 도달한 카운트.
visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True
queue = deque()
queue.append((0, 0, 0, 0))
answer = -1
while queue:
    i, j, k, cnt = queue.popleft()

    if i == N - 1 and j == M - 1:
        answer = cnt
        break

    for x in range(4):
        ni, nj = i + di2[x], j + dj2[x]
        if 0 <= ni < N and 0 <= nj < M:
            if not visited[ni][nj][k] and matrix[ni][nj] == 0:
                visited[ni][nj][k] = True
                queue.append((ni, nj, k, cnt + 1))
    if k == K:
        continue

    for x in range(8):
        ni, nj = i + di1[x], j + dj1[x]
        if 0 <= ni < N and 0 <= nj < M:
            if not visited[ni][nj][k + 1] and matrix[ni][nj] == 0:
                visited[ni][nj][k + 1] = True
                queue.append((ni, nj, k + 1, cnt + 1))
print(answer)
