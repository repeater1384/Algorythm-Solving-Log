def matrix_mul(a, b, _size=2):
    # return multiplication of a and b in a matrix
    # a, b is square matrices, their size is _size
    _result = [[0] * _size for _ in range(_size)]

    for i in range(_size):
        for j in range(_size):
            for k in range(_size):
                _result[i][j] += a[i][k] * b[k][j]

    for i in range(_size):
        for j in range(_size):
            _result[i][j] %= 1_000_000_007

    return _result


n = int(input())
A = [[1, 1], [1, 0]]
result = [[1, 0], [0, 1]]

while n:
    if n & 1:
        result = matrix_mul(result, A)
    A = matrix_mul(A, A)
    n //= 2

print(result[1][0])
