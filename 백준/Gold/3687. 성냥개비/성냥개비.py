min_val = [float('inf')] * 101
max_val = [0] * 101
min_val[2:8] = [1, 7, 4, 2, 6, 8]

# fill max_val
for i in range(2, 101):
    if i % 2 == 0:
        max_val[i] = '1' * (i // 2)
    else:
        max_val[i] = '7' + '1' * ((i - 2) // 2)

# fill min_val
nums = [-1, -1, 1, 7, 4, 2, 0, 8]
for i in range(8, 101):
    for j in range(2, 8):
        min_val[i] = min(min_val[i], min_val[i - j] * 10 + nums[j])

for _ in range(int(input())):
    n = int(input())
    print(min_val[n], max_val[n])
