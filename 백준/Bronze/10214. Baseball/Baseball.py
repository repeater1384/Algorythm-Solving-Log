for _ in range(int(input())):
    ys = ks = 0

    for _ in range(9):
        y, k = map(int, input().split())
        ys += y
        ks += k

    if ys == ks:
        print('Draw')
    elif ys > ks:
        print('Yonsei')
    else:
        print('Korea')
