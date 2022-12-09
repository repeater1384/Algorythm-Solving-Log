min_num, max_num = map(int, input().split())

matrix = [1 for _ in range(min_num, max_num + 1)]
square_roots = [i * i for i in range(2, int(max_num ** .5) + 1)]

for square_root in square_roots:
    cur_idx = ((min_num - 1) // square_root + 1) * square_root - min_num
    while cur_idx <= max_num - min_num:
        matrix[cur_idx] = 0
        cur_idx += square_root

print(sum(matrix))
