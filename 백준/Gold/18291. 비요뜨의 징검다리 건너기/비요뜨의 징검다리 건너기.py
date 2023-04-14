import sys

input = sys.stdin.readline


def fast_power(a, b):
    result = 1
    p = int(1e9 + 7)
    while b > 0:
        if b & 1:
            result = result * a % p
        a = a * a % p
        b //= 2
    return result


for _ in range(int(input())):
    print(fast_power(2, int(input()) - 2))
