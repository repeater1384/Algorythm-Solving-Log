while True:
    data = input()
    if data == '#':
        break
    target = data[0]
    print(target,data.lower().count(target)-1)