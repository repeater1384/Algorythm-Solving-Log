k = int(input())

info = [[*map(int, input().split())] for _ in range(6)]

dir = [*zip(*info)][0]
max_x, max_y, diff_x, diff_y = [0] * 4

for d, n in info:
    if d == 1 or d == 2:
        max_x = max(max_x, n)
    else:
        max_y = max(max_y, n)

temp = []
for i in range(1, 5):
    if dir.count(i) == 2:
        temp.append(i)
new_info = info + info[:3]

answer = max_x * max_y
for i in range(6):
    a = []
    for d in new_info[i:i + 4]:
        a.append(d[0])
    if a == temp + temp or a == temp[::-1] * 2:
        diff_area = 1
        for di in range(1, 3):
            diff_area *= new_info[i + di][1]
        break
print((answer - diff_area) * k)
