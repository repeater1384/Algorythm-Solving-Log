from itertools import combinations

T = int(input())

for _ in range(T):
    N = int(input())
    coordinates = [[*map(int, input().split())] for _ in range(N)]

    answer = float('inf')
    for will_add in map(set, combinations(range(N), N // 2)):
        will_minus = set(range(N)) - will_add

        x1, x2, y1, y2 = 0, 0, 0, 0
        for add_idx in will_add:
            x, y = coordinates[add_idx]
            x1 += x
            y1 += y

        for minus_idx in will_minus:
            x, y = coordinates[minus_idx]
            x2 += x
            y2 += y
        dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5
        answer = min(answer, dis)
    print(answer)
