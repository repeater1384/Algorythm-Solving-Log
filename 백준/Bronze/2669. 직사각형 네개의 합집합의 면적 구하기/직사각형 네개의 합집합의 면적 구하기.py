matrix = [[0] * 101 for _ in range(101)]
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for y in range(b, d):
        for x in range(a, c):
            matrix[y][x] = 1

print(sum(map(lambda x: sum(x), matrix)))
