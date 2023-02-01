while True:
    try:
        N = int(input())
    except EOFError:
        break
    cur = 1
    while True:
        if cur % N == 0:
            print(len(str(cur)))
            break
        cur = cur * 10 + 1
