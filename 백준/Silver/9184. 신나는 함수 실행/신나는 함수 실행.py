dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]


def w(_a, _b, _c):
    if _a <= 0 or _b <= 0 or _c <= 0:
        return 1
    if _a > 20 or _b > 20 or _c > 20:
        return w(20, 20, 20)

    if dp[_a][_b][_c] == 0:
        if _a < _b < _c:
            dp[_a][_b][_c] = w(_a, _b, _c - 1) + w(_a, _b - 1, _c - 1) - w(_a, _b - 1, _c)
        else:
            dp[_a][_b][_c] = w(_a - 1, _b, _c) + w(_a - 1, _b - 1, _c) + w(_a - 1, _b, _c - 1) - w(_a - 1, _b - 1,
                                                                                                   _c - 1)
    return dp[_a][_b][_c]


while True:
    a, b, c = map(int, input().split())

    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
