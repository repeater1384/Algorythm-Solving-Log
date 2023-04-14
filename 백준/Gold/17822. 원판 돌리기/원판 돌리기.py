N, M, T = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())
    if d == 0:
        k = M - k
    for i in range(x - 1, N, x):
        matrix[i] = matrix[i][k:] + matrix[i][:k]

    remove_list = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'X':
                continue
            j1, j2 = (j + M - 1) % M, (j + M + 1) % M
            if matrix[i][j] == matrix[i][j1]:
                remove_list.append([i, j])
                remove_list.append([i, j1])
            if matrix[i][j] == matrix[i][j2]:
                remove_list.append([i, j])
                remove_list.append([i, j2])
            if i > 0:
                i1 = i - 1
                if matrix[i][j] == matrix[i1][j]:
                    remove_list.append([i, j])
                    remove_list.append([i1, j])
            if i < N - 1:
                i2 = i + 1
                if matrix[i][j] == matrix[i2][j]:
                    remove_list.append([i, j])
                    remove_list.append([i2, j])

    if remove_list:
        for i, j in remove_list:
            matrix[i][j] = 'X'
    else:
        cnt = 0
        avg = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] != 'X':
                    cnt += 1
                    avg += matrix[i][j]
        if cnt != 0:
            avg /= cnt
        for i in range(N):
            for j in range(M):
                if matrix[i][j] != 'X':
                    if matrix[i][j] > avg:
                        matrix[i][j] -= 1
                    elif matrix[i][j] < avg:
                        matrix[i][j] += 1
answer = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] != 'X':
            answer += matrix[i][j]
print(answer)
