N, M = map(int, input().split())
matrix = [[*input()] for _ in range(N)]
parents = [i for i in range(N * M)]


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


d = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}

for i in range(N):
    for j in range(M):
        di, dj = d[matrix[i][j]]
        ni, nj = i + di, j + dj
        union(i * M + j, ni * M + nj)
print(len(set(map(lambda x: find(x), parents))))
