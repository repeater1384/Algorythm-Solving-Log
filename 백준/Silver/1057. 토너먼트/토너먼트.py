from math import log2

n, a, b = map(int, input().split())

for round in range(1, int(log2(n)) + 2):
    if abs(a - b) == 1 and min(a, b) % 2:
        print(round)
        break
    a = (a + 1) // 2
    b = (b + 1) // 2
