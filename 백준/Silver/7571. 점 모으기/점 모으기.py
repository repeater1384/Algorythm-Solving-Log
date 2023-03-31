import sys


def get_differ(_x, _y, _dx, _dy):
    return abs(_dx - _x) + abs(_dy - _y)


N, M = map(int, sys.stdin.readline().split())

x_positions = []
y_positions = []

for _ in range(M):
    y, x = map(int, sys.stdin.readline().split())
    x_positions.append(x)
    y_positions.append(y)

x_mid = sorted(x_positions)[M // 2]
y_mid = sorted(y_positions)[M // 2]
answer = 0

for x, y in zip(x_positions, y_positions):
    answer += get_differ(x, y, x_mid, y_mid)

print(answer)
