import sys

input = sys.stdin.readline

N = int(input())

# 색상, 크기, 인덱스
balls = sorted([[*map(int, input().split()), i] for i in range(N)], key=lambda x: (x[1], x[0]))

answers = [0] * N
color_prefix_sum = [0] * (N + 1)  # 색 별 누적합
all_prefix_sum = 0  # 전체 누적합
j = 0

for i in range(N):
    i_color, i_size, index = balls[i]
    while True:
        j_color, j_size, _ = balls[j]
        if i_size <= j_size: break

        color_prefix_sum[j_color] += j_size
        all_prefix_sum += j_size
        j += 1

    answers[index] = all_prefix_sum - color_prefix_sum[i_color]
print(*answers, sep='\n')
