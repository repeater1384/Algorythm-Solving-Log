def solve():
    n = int(input())

    matrix = [[*map(int, input().split())] for _ in range(2)]

    if n > 1:
        matrix[0][1] += matrix[1][0]
        matrix[1][1] += matrix[0][0]
    for i in range(2, n):
        matrix[0][i] += max(matrix[1][i - 1], matrix[1][i - 2])
        matrix[1][i] += max(matrix[0][i - 1], matrix[0][i - 2])
        
    return max(matrix[0][-1], matrix[1][-1])


for _ in range(int(input())):
    print(solve())
