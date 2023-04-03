def drop(table, t, x):
    if t == 1:
        for i in range(7):
            if i == 6 or table[i][x] != 0:
                table[i - 1][x] = 1
                break
    elif t == 2:
        for i in range(7):
            if i == 6 or table[i][x] != 0:
                table[i - 1][x] = 1
                table[i - 2][x] = 1
                break
    elif t == 3:
        for i in range(7):
            if i == 6 or table[i][x] != 0 or table[i][x + 1] != 0:
                table[i - 1][x] = table[i - 1][x + 1] = 1
                break


def scoring(table):
    score = 0
    # 꽉 찬 줄 지우기
    for i in range(2, 6):
        if sum(table[i]) == 4:
            score += 1
            for j in range(i, 0, -1):
                for k in range(4):
                    table[j][k] = table[j - 1][k]
            for k in range(4):
                table[0][k] = 0
    # 연한 칸 내리기
    down = (1 if sum(table[0]) > 0 else 0) + (1 if sum(table[1]) > 0 else 0)
    if down > 0:
        for i in range(5 - down, -1, -1):
            for j in range(4):
                table[i + down][j] = table[i][j]

        for i in range(down):
            for j in range(4):
                table[i][j] = 0
    return score


def counting(table):
    return sum([sum(row) for row in table])


N = int(input())

score = 0
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]

for _ in range(N):
    t, x, y = map(int, input().split())
    drop(green, t, x)
    drop(blue, [_, 1, 3, 2][t], y)
    score += scoring(green)
    score += scoring(blue)

print(score)
print(counting(green) + counting(blue))
