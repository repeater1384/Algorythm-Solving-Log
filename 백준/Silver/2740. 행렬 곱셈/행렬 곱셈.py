def get_num_with_row(matrix, row):
    return matrix[row]


def get_num_with_col(matrix, col):
    res = []
    for row in range(len(matrix)):
        res.append(matrix[row][col])
    return res


N, M = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]

_, K = map(int, input().split())
B = [[*map(int, input().split())] for _ in range(M)]

result = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        result[i][j] = sum([a * b for a, b in zip(get_num_with_row(A, i), get_num_with_col(B, j))])

for i in range(N):
    print(*result[i])
