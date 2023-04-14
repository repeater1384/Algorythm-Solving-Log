size = int(input())
matrix = [[*map(int, input().split())] for _ in range(size)]

answer = [0,0]
def division(_matrix, size, x, y):
    global answer
    if size == 1:
        answer[_matrix[y][x]] +=1
        return
    check = _matrix[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if check != _matrix[i][j]:  # 잘라야할때,
                division(_matrix, size // 2, x, y)
                division(_matrix, size // 2, x + size // 2, y)
                division(_matrix, size // 2, x, y + size // 2)
                division(_matrix, size // 2, x + size // 2, y + size // 2)
                return
    #똑같으면
    answer[check] +=1

division(matrix,size,0,0)
print(*answer,sep='\n')