import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
new_matrix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        new_matrix[i][j] = matrix[i - 1][j - 1] + new_matrix[i - 1][j] + new_matrix[i][j - 1] - new_matrix[i - 1][j - 1]
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(new_matrix[x][y] - new_matrix[x][j - 1] - new_matrix[i - 1][y] + new_matrix[i - 1][j - 1])
