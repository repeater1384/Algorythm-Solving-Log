def fibo(n):
    a, b = 0, 1
    while n - 1:
        n -= 1
        a, b = b, a + b
    return b


print(fibo(int(input())))