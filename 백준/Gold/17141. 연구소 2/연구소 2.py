from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
processed_matrix = [[-1] * N for _ in range(N)]
virius_list = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            virius_list.append((i, j))
            # processed_matrix[i][j] = '*'
        elif matrix[i][j] == 1:
            processed_matrix[i][j] = '-'


def combination(_virus_list, idx):
    for i in range(len(_virus_list)):
        if idx == 1:
            yield [_virus_list[i]]
        else:
            for next in combination(_virus_list[i + 1:], idx - 1):
                yield [_virus_list[i]] + next


def bfs(_combed_virus_list):
    _processed_matrix = deepcopy(processed_matrix)
    for virus_pos in _combed_virus_list:
        _processed_matrix[virus_pos[0]][virus_pos[1]] = 0

    queue = deque(_combed_virus_list)
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    _result = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if _processed_matrix[ny][nx] == -1 and _processed_matrix[ny][nx] != '_':
                    _processed_matrix[ny][nx] = _processed_matrix[y][x] + 1
                    _result = max(_processed_matrix[ny][nx], _result)
                    queue.append([ny, nx])

    if list(sum(_processed_matrix, [])).count(-1) == 0:
        return _result
    return N * N


answer = N * N
for comb in combination(virius_list, M):
    result = bfs(comb)
    answer = min(answer, result)
print(answer if answer != N * N else -1)
