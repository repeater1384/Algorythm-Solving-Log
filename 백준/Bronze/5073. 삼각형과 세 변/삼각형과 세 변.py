while True:
    a, b, c = sorted([*map(int, input().split())])
    if a == b == c == 0:
        break
    answer = 'Invalid' if a + b <= c else ['', 'Equilateral', 'Isosceles', 'Scalene'][len(set([a, b, c]))]
    print(answer)
