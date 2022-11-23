def solution(N, M, queries):
    answer = []

    table = [[0] * M for _ in range(N)]
    n = 1
    for i in range(N):
        for j in range(M):
            table[i][j] = n
            n += 1
    for y1, x1, y2, x2 in queries:
        answer.append(rotate(*map(lambda x: x - 1, [y1, x1, y2, x2]), table))
    return answer


def rotate(y1, x1, y2, x2, table):
    temp = table[y1][x1]
    arr = [temp]
    for y in range(y1, y2):
        table[y][x1] = table[y + 1][x1]
        arr.append(table[y][x1])
    for x in range(x1, x2):
        table[y2][x] = table[y2][x + 1]
        arr.append(table[y2][x])
    for y in range(y2, y1, -1):
        table[y][x2] = table[y - 1][x2]
        arr.append(table[y][x2])
    for x in range(x2, x1, -1):
        table[y1][x] = table[y1][x - 1]
        arr.append(table[y1][x])
    table[y1][x1 + 1] = temp
    return min(arr)