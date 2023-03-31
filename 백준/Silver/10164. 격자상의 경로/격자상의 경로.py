n, m, k = map(int, input().split())


def get(x1, y1, x2, y2):
    def fac(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    x = x2 - x1
    y = y2 - y1
    return fac(x + y) // (fac(x) * fac(y))


if k:
    y, x = (k - 1) // m, (k - 1) % m
    print(get(0, 0, x, y) * (get(x, y, m - 1, n - 1)))
else:
    print(get(0, 0, m - 1, n - 1))
