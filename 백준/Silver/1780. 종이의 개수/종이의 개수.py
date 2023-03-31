size = int(input())
matrix = [[*map(int, input().split())] for _ in range(size)]

answer = [0, 0, 0]


def division(_matrix, size, x, y):
    global answer
    if size == 1:
        answer[_matrix[y][x]+1] += 1
        return
    check = _matrix[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if check != _matrix[i][j]:  # 잘라야할때,
                newsize = size // 3
                division(_matrix, size // 3, x, y)
                division(_matrix, size // 3, x + newsize, y)
                division(_matrix, size // 3, x + 2 * newsize, y)
                division(_matrix, size // 3, x, y + newsize)
                division(_matrix, size // 3, x + newsize, y + newsize)
                division(_matrix, size // 3, x + 2 * newsize, y + newsize)
                division(_matrix, size // 3, x, y + 2 * newsize)
                division(_matrix, size // 3, x + newsize, y + 2 * newsize)
                division(_matrix, size // 3, x + 2 * newsize, y + 2 * newsize)
                return
    # 똑같으면
    answer[check+1] += 1


division(matrix, size, 0, 0)
print(*answer, sep='\n')
