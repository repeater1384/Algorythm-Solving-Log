N, M = map(int, input().split())
matrix = [[*input()] for _ in range(N)]

di, dj = [-1, 1, 0, 0], [0, 0, 1, -1]

answer = 'No'


def dfs(ci, cj, si, sj, depth):
    global answer

    for k in range(4):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if matrix[ni][nj] == matrix[si][sj]:
                if ni == si and nj == sj and depth >= 3:
                    answer = 'Yes'
                    return True
                if not visited[ni][nj]:
                    visited[ni][nj] = True
                    if dfs(ni, nj, si, sj, depth + 1):
                        return True
                    visited[ni][nj] = False


for i in range(N):
    for j in range(M):
        if answer == 'Yes':
            continue
        visited = [[False] * M for _ in range(N)]
        visited[i][j] = True
        dfs(i, j, i, j, 1)
print(answer)
