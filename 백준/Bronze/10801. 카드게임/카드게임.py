a, b = 0, 0
for i, j in zip(map(int, input().split()), map(int, input().split())):
    if i > j: a += 1
    if i < j: b += 1

if a == b:
    print('D')
elif a>b:
    print('A')
else:
    print('B')