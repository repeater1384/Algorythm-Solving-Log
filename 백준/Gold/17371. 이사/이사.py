N = int(input())
pos_arr = [[*map(int, input().split())] for _ in range(N)]

min_dis = 1e9
answer_i, answer_j = -1, -1
for i, (x1, y1) in enumerate(pos_arr):
    max_dis = 0
    for j, (x2, y2) in enumerate(pos_arr):
        cur_dis = (y2 - y1) ** 2 + (x2 - x1) ** 2
        if max_dis < cur_dis:
            max_dis = cur_dis
            answer_j = j
    if min_dis > max_dis:
        min_dis = max_dis
        answer_i = i

print(*pos_arr[answer_i])
