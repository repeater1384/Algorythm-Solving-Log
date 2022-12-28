def multiply_matrix(A, B):
    # return matrix A*B
    row = len(A)
    col = len(B[0])
    same = len(A[0])
    result = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            for k in range(same):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= MOD
    return result


def pow_matrix(A, B):
    # return matrix A^B
    result = [[0] * len(A) for _ in range(len(A))]
    for i in range(len(A)):
        result[i][i] = 1

    while B:
        if B & 1:
            result = multiply_matrix(result, A)
            B -= 1
        B //= 2
        A = multiply_matrix(A, A)
    return result


adj_matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]
MOD = 1_000_000_007

D = int(input())
final_adj_matrix = pow_matrix(adj_matrix, D)
print(final_adj_matrix[0][0])
