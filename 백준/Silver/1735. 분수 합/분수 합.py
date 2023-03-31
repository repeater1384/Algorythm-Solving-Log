def gcd(a, b):
    a, b = max(a, b), min(a, b)

    while b:
        r = a % b
        a, b = b, r

    return a


x, y = map(int, input().split())
n, m = map(int, input().split())

molecule = x * m + y * n
denominator = y * m
GCD = gcd(molecule, denominator)
molecule, denominator = molecule // GCD, denominator // GCD
print(molecule, denominator)
