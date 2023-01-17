N, M = map(int, input().split())
orig_matrix = [[*map(int, input())] for _ in range(N)]
target_matrix = [[*map(int, input())] for _ in range(N)]

answer = 0
for i in range(N - 2):
    for j in range(M - 2):
        if orig_matrix[i][j] == target_matrix[i][j]:
            continue
        answer += 1
        for di in range(3):
            for dj in range(3):
                orig_matrix[i + di][j + dj] ^= 1


for i in range(N):
    for j in range(M):
        if orig_matrix[i][j] != target_matrix[i][j]:
            answer = -1
            break
print(answer)
