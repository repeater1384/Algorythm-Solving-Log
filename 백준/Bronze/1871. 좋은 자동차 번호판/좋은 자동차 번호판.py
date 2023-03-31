for _ in range(int(input())):
    a, b = input().split('-')
    print('nice' if abs(int(b) - sum([(ord(c) - 65) * (26 ** i) for i, c in enumerate(a[::-1])])) <= 100 else 'not nice')
