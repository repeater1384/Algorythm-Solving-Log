def print_all_prime(num):
    primes = set()

    for i in range(1,int(num ** .5) + 1):
        if num % i == 0:
            primes.add(i)
            primes.add(num // i)

    print(*sorted(primes), sep='\n')


n = int(input())

if n == 2:
    a, b = map(int, input().split())

    a, b = (a, b) if a > b else (b, a)

    while b:
        r = a % b
        a = b
        b = r

    print_all_prime(a)
else:
    a, b, c = map(int, input().split())

    a, b = (a, b) if a > b else (b, a)

    while b:
        r = a % b
        a = b
        b = r

    b = c

    a, b = (a, b) if a > b else (b, a)

    while b:
        r = a % b
        a = b
        b = r

    print_all_prime(a)
