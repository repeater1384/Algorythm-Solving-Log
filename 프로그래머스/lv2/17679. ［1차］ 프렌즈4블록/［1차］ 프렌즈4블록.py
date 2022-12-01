def solution(N, M, board):
    board = [[*row] for row in board]
    while True:
        cant_remove = True
        will_remove = [[False] * M for _ in range(N)]
        for i in range(N - 1):
            for j in range(M - 1):
                if board[i][j] == ' ':
                    continue
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    will_remove[i][j] = True
                    will_remove[i + 1][j] = True
                    will_remove[i][j + 1] = True
                    will_remove[i + 1][j + 1] = True
                    cant_remove = False

        for i in range(N):
            for j in range(M):
                if will_remove[i][j]:
                    board[i][j] = ' '

        next_board = [[' ']*M for _ in range(N)]
        for j in range(M):
            temp = []
            for i in range(N):
                if board[i][j] == ' ':
                    continue
                temp.append(board[i][j])
            idx = N-1
            while temp:
                next_board[idx][j] = temp.pop()
                idx -= 1
        board = next_board
        if cant_remove:
            break
    answer = N * M
    for i in range(N):
        for j in range(M):
            if board[i][j] == ' ':
                continue
            answer -= 1
    return answer

