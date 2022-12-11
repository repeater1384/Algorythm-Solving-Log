N, M = map(int, input().split())
matrix = [[*input()] for _ in range(N)]
parents = [i for i in range(N * M)]


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


def conv_pos(*pos):
    if len(pos) == 2:
        return pos[0] * M + pos[1]
    return pos[0] // M, pos[0] % M


for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'D':
            ni, nj = i + 1, j
        if matrix[i][j] == 'L':
            ni, nj = i, j - 1
        if matrix[i][j] == 'R':
            ni, nj = i, j + 1
        if matrix[i][j] == 'U':
            ni, nj = i - 1, j
        pos1 = conv_pos(i, j)
        pos2 = conv_pos(ni, nj)
        union(pos1, pos2)
        
print(len(set(map(lambda x: find(x), parents))))
