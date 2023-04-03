def solution(N):
    if(N==1):
        print('*',end='')
        return
    for i in range(N*2):
        starTurn = not i % 2
        for j in range(N):
            if(starTurn):
                print('*',end='')
                starTurn = 0
            else:
                if not j == N-1:
                    print(' ',end='')
                starTurn = 1

        if(not i==N*2 - 1):print()

solution(int(input()))