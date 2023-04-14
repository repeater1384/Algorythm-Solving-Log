def del_num(board,num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                board[i][j] = 0
                return board
    return


def check_bingo(board):
    size = len(board)
    bingo = 0
    for i in range(size):
        count = 0
        for j in range(size):
            if board[i][j] == 0:count += 1
        if count == size:
            bingo +=1

    for i in range(size):
        count = 0
        for j in range(size):
            if board[j][i] == 0:count += 1
        if count == size:
            bingo +=1

    count = 0
    for i in range(size):
        if board[i][i] == 0:
            count +=1
    if count == size:
        bingo +=1

    count = 0
    for i in range(size):
        if board[i][size-i-1] == 0:
            count +=1
    if count == size:
        bingo +=1

    return bingo


board = [[*map(int,input().split())] for _ in range(5)]
call = []

for _ in range(5):call += [*map(int,input().split())]

for idx,c in enumerate(call):
    board = del_num(board,c)
    bingo = check_bingo(board)
    if bingo >= 3:
        print(idx+1)
        break