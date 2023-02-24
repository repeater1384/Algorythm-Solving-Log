N = int(input())
board = [[*map(int, input().split())] for _ in range(N)]
answer = 0


def rotate(old_board):
    new_board = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            new_board[c][N - r - 1] = old_board[r][c]

    return new_board


def merge(old_board):
    merged_board = []
    for row in range(N):
        temp = [i for i in old_board[row] if i != 0]
        for i in range(1, len(temp)):
            if temp[i - 1] == temp[i]:
                temp[i - 1] *= 2
                temp[i] = 0
        temp = [i for i in temp if i != 0]
        merged_board.append(temp + [0] * (N - len(temp)))

    return merged_board


def dfs(depth, cur_board):
    global answer

    cur_max_value = max(max(row) for row in cur_board)

    if depth == 5:
        answer = max(answer, cur_max_value)
        return

    for _ in range(4):
        merged_board = merge(cur_board)
        dfs(depth + 1, merged_board)
        cur_board = rotate(cur_board)


dfs(0, board)
print(answer)
