board = [input() for _ in range(8)]
white = 1
answer =0
for b in board:
    for k in b:
        if white % 2 and k == 'F':
            answer+=1
        white +=1
    white += 1
print(answer)