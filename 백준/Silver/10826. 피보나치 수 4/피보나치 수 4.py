def get_fibo(n):
    a, b = 0, 1
    while n:
        a, b = b, a + b
        n -= 1
    return a


n = int(input())
print(get_fibo(n))
