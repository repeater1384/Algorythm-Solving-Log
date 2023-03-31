def get_change_count(_board):
    start_B = 0
    start_W = 0

    for i in range(8):
        for j in range(8):
            if i % 2 == j % 2:
                if _board[j][i] == 'W':
                    start_B += 1
                else:
                    start_W += 1
            else:
                if _board[j][i] == 'W':
                    start_W += 1
                else:
                    start_B += 1

    return min(start_B, start_W)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

answer = 64
for j in range(N - 7):
    for i in range(M - 7):
        sliced_board = [board[j + idx][i:i + 8] for idx in range(8)]
        answer = min(answer, get_change_count(sliced_board))

print(answer)
