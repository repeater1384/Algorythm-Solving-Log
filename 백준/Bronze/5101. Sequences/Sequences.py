while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0: break

    temp = (c - a) // b + 1
    print(temp if (c - a) % b == 0 and temp > 0 else 'X')
