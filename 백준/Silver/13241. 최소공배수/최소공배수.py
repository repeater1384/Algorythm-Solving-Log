def get_gcd(a, b):
    a, b = (a, b) if a > b else (b, a)

    while b:
        a, b = b, a % b

    return a


A, B = map(int, input().split())
gcd = get_gcd(A, B)
print(A * B // gcd)
