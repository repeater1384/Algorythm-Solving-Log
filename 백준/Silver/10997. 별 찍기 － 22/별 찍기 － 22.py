N = int(input())

width = 4 * N - 3
height = 4 * N - 1

stars = [[' ' for _ in range(width)] for _ in range(height)]


def fill_star(n, x, y):
    if n == 1:
        stars[y][x] = '*'
        stars[y + 1][x] = '*'
        stars[y + 2][x] = '*'

        # for i in range(3):
        #     stars[y + i][x] = '*'
    else:
        for i in range(4 * n - 4):
            stars[y][x] = '*'
            x -= 1
        for i in range(4 * n - 2):
            stars[y][x] = '*'
            y += 1

        for i in range(4 * n - 4):
            stars[y][x] = '*'
            x += 1

        for i in range(4 * n - 4):
            stars[y][x] = '*'
            y -= 1

        stars[y][x] = '*'
        stars[y][x - 1] = '*'
        fill_star(n - 1, x - 2, y)


if N == 1:
    print('*')

else:
    fill_star(N, width - 1, 0)

    for k in stars:
        print(''.join(k).rstrip())
