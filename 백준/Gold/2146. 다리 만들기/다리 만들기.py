from collections import deque

N = int(input())
matrix = [[*map(int, input().split())] for _ in range(N)]

island_num = 0
island_matrix = [[-1] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
island_list = {}
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            island_list[island_num] = []
            queue = deque()
            visited[i][j] = True
            queue.append((i, j))
            while queue:
                ci, cj = queue.popleft()
                island_matrix[ci][cj] = island_num
                is_outer = False
                for k in range(4):
                    ni, nj = ci + di[k], cj + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if matrix[ni][nj] == 1 and not visited[ni][nj]:
                            queue.append((ni, nj))
                            visited[ni][nj] = True
                        if matrix[ni][nj] == 0:
                            is_outer = True
                if is_outer:
                    island_list[island_num].append((ci, cj))

            island_num += 1
answer = float('inf')
for cur_island_num, outer in island_list.items():
    visited = [[False] * N for _ in range(N)]
    queue = deque()
    for i, j in outer:
        visited[i][j] = True
        queue.append((i, j, 0))

    while queue:
        ci, cj, cnt = queue.popleft()
        if island_matrix[ci][cj] >= 0 and island_matrix[ci][cj] != cur_island_num:
            answer = min(answer, cnt - 1)
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if island_matrix[ni][nj] == cur_island_num:
                    queue.append((ni, nj, cnt))
                    visited[ni][nj] = True
                else:
                    queue.append((ni, nj, cnt + 1))
                    visited[ni][nj] = True

print(answer)
