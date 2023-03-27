N, M = map(int, input().split())
matrix = [[*input()] for _ in range(N)]
answer = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] != '.':
            continue
        if (j == 0 or matrix[i][j - 1] == '#') and matrix[i][j:j + 3] == ['.', '.', '.']:
            answer.append(f'{i + 1} {j + 1}')
            continue
        if (i == 0 or matrix[i - 1][j] == '#') and [*map(lambda x: list(x), zip(*matrix[i:i + 3]))][j] == ['.', '.',
                                                                                                           '.']:
            answer.append(f'{i + 1} {j + 1}')
print(len(answer))
print(*answer, sep='\n')
