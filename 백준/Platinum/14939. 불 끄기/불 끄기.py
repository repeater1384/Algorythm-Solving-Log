from copy import deepcopy

matrix = [[*map(lambda x: 1 if x == 'O' else 0, input())] for _ in range(10)]
di, dj = [1, -1, 0, 0, 0], [0, 0, 1, -1, 0]
answer = float('inf')


def press_button(i, j):
    global copy_matrix
    for k in range(5):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < 10 and 0 <= nj < 10:
            copy_matrix[ni][nj] ^= 1


for case in range(1 << 10):
    copy_matrix = deepcopy(matrix)
    count = 0

    # 첫번째 줄 case에 맞춰서 누르기
    for j in range(10):
        if case & (1 << j):
            press_button(0, j)
            count += 1

    # 두번째 줄부터, 마지막 줄까지 바로 위 칸 켜져 있으면 누르기
    # 바로 위 칸(i-1, j)을 끄려면 (i, j)룰 누르는 방법 뿐이다.
    for i in range(1, 10):
        for j in range(10):
            if copy_matrix[i - 1][j]:
                press_button(i, j)
                count += 1

    # 마지막 줄이 다 꺼져 있다면 성공!
    if sum(copy_matrix[10 - 1]) == 0:
        answer = min(answer, count)

print(answer if answer != float('inf') else -1)
