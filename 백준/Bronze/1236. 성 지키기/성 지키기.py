N, M = map(int, input().split())

matrix = [[*input()] for _ in range(N)]

empty_vertical = N
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'X':
            empty_vertical -= 1
            break

empty_horizontal = M

for j in range(M):
    for i in range(N):
        if matrix[i][j] == 'X':
            empty_horizontal -= 1
            break

print(max(empty_vertical, empty_horizontal))
