for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,input().split(' '))

    if r1>r2:
        x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1
    d = pow((x2-x1)**2 + (y2-y1)**2,0.5)
    # print(x1, y1, r1, x2, y2, r2, d)
    if d == 0.0 and r2 == r1: print(-1)
    elif r2-r1 < d and d < r2+r1 : print(2)
    elif r2-r1 == d or r2+r1 == d:print(1)
    elif r2+r1 < d or d<r2-r1: print(0)
