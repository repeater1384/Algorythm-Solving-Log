import sys

input = sys.stdin.readline

r, c, q = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(r)]
new_matrix = [[0] * (c + 1) for _ in range(r + 1)]

for i in range(1, r + 1):
    for j in range(1, c + 1):
        new_matrix[i][j] = matrix[i - 1][j - 1] + new_matrix[i - 1][j] + new_matrix[i][j - 1] - new_matrix[i - 1][j - 1]
for _ in range(q):
    i, j, x, y = map(int, input().split())
    total_sum = new_matrix[x][y] - new_matrix[x][j - 1] - new_matrix[i - 1][y] + new_matrix[i - 1][j - 1]
    total_count = (x - i + 1) * (y - j + 1)
    print(total_sum // total_count)
