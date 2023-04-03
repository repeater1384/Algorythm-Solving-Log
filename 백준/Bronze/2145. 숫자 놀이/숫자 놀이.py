while True:
    num = int(input())
    if num == 0:
        break

    while True:
        if len(str(num)) == 1:
            break
        num = sum(map(int, str(num)))

    print(num)
   