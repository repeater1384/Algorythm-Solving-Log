N, M = map(int, input().split())
matrix = [[*map(int, input())] for _ in range(N)]


def get_sequence():
    global answer
    num = matrix[si][sj]
    if check_squre(num):
        answer = max(answer, num)
    di2, dj2 = di, dj
    while True:
        ni, nj = si + di2 * jump1, sj + dj2 * jump2
        if 0 <= ni < N and 0 <= nj < M:
            num = num * 10 + matrix[ni][nj]
            if check_squre(num):
                answer = max(answer, num)
            di2 += di
            dj2 += dj
        else:
            return


def check_squre(num):
    return num ** .5 == int(num ** .5)


answer = answer = max([matrix[i][j] for i in range(N) for j in range(M) if check_squre(matrix[i][j])]+[-1])
for si in range(N):
    for sj in range(M):
        for jump1 in range(N):
            for jump2 in range(M):
                if jump1 == jump2 == 0:
                    continue
                for di, dj in zip([-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]):
                    if (jump1 == 0 and dj == 0) or (jump2 == 0 and di == 0):
                        continue
                    get_sequence()

print(answer)
