data = input()


def check(_data):
    s, e = 0, len(_data) - 1
    while s < e:
        if _data[s] != _data[e]:
            return False
        s += 1
        e -= 1
    return True


surfix = ''
idx = 1
while True:
    if check(data + surfix):
        print(len(data + surfix))
        break
    surfix = data[:idx][::-1]
    idx += 1
