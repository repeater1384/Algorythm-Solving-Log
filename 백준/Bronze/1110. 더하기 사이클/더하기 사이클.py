N = int(input())

cur_num = N
repeated = 0
while True:
    repeated += 1
    cur_num = cur_num % 10 * 10 + sum(map(int, str(cur_num))) % 10
    if N == cur_num:
        print(repeated)
        break
