def matrix_mul_2_2(a, b):
    _result = [[0] * 2 for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                _result[i][j] += a[i][k] * b[k][j]

    for i in range(2):
        for j in range(2):
            _result[i][j] %= 1_000_000_007

    return _result


n = (int(input()) + 1) // 2 * 2
A = [[1, 1], [1, 0]]
result = [[1, 0], [0, 1]]

while n:
    if n & 1:
        result = matrix_mul_2_2(result, A)
    A = matrix_mul_2_2(A, A)
    n //= 2

print(result[1][0])
