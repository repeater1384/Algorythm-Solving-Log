def check(s, e, flag):
    while s <= e:
        if data[s] == data[e]:
            s += 1
            e -= 1
        else:
            if flag or check(s + 1, e, True) * check(s, e - 1, True) != 0:
                return 2
            else:
                return 1
    return 0


for _ in range(int(input())):
    data = input()
    print(check(0, len(data) - 1, False))
