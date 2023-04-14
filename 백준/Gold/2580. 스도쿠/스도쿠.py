from sys import exit
matrix = [[*map(int, input().split())] for _ in range(9)]
zero_list = [(i, j) for i in range(9) for j in range(9) if matrix[i][j] == 0]


def get_possible_list(i, j):
    possible_list = set(map(int, '123456789'))
    row_list = set(matrix[i])
    col_list = set([matrix[_i][j] for _i in range(9)])
    box_list = set(
        [matrix[_i][_j] for _i in range(i // 3 * 3, i // 3 * 3 + 3) for _j in range(j // 3 * 3, j // 3 * 3 + 3)])

    return possible_list - row_list - col_list - box_list


def dfs(idx):
    if idx == len(zero_list):
        for i in range(9):
            print(' '.join(map(str,matrix[i])))
        exit()

    i, j = zero_list[idx]
    possible_list = get_possible_list(i, j)
    for num in possible_list:
        matrix[i][j] = num
        dfs(idx + 1)
        matrix[i][j] = 0


dfs(0)
