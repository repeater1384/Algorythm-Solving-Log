def max_continuous_len(one_line):
    value = 0
    cur = None
    temp = 1
    for a in one_line + '_':
        if cur == a:
            temp += 1
        else:
            value = max(value, temp)
            cur = a
            temp = 1
    return value


N = int(input())

matrix = [[*input()] for _ in range(N)]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

answer = 0

for xy in range(N):
    answer = max(answer, max_continuous_len(''.join(matrix[xy])), max_continuous_len(''.join([*zip(*matrix)][xy])))
    
for y in range(N):
    for x in range(N):
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and matrix[ny][nx] != matrix[y][x]:
                matrix[ny][nx], matrix[y][x] = matrix[y][x], matrix[ny][nx]
                answer = max(answer,
                             max_continuous_len(''.join(matrix[y])),
                             max_continuous_len(''.join(matrix[ny])),
                             max_continuous_len(''.join([*zip(*matrix)][x])),
                             max_continuous_len(''.join([*zip(*matrix)][nx])))
                matrix[ny][nx], matrix[y][x] = matrix[y][x], matrix[ny][nx]
print(answer)
