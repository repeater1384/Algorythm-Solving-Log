N = int(input())
calls = [*map(int, input().split())]

Y = sum([10 * (c // 30 + 1) for c in calls])
M = sum([15 * (c // 60 + 1) for c in calls])

if Y < M:
    print('Y',Y)
elif M < Y:
    print('M',M)
else:
    print('Y','M',Y)

