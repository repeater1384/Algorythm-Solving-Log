def fast_power(a, b, c):
    if b == 0:
        return 1

    if b % 2 == 0:
        temp = fast_power(a, b // 2, c)
        return temp * temp % c
    else:
        temp = fast_power(a, (b - 1) // 2, c)
        return a * temp * temp % c


print(fast_power(*map(int,input().split())))
