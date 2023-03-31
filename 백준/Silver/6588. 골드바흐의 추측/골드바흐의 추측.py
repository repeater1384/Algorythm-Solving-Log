import sys


def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [[i for i in range(2, n) if sieve[i]], sieve]


temp = prime_list(1000000)
arr = temp[0]
is_prime = temp[1]


def sosu(n):
    for i in range(1, len(arr)):
        if arr[i] > n / 2:
            print("Goldbach's conjecture is wrong.")
            return 0, 0
        if is_prime[n - arr[i]]:
            return arr[i], n - arr[i]


while True:
    n = int(sys.stdin.readline())
    if n:
        a, b = sosu(n)
        if a == b == 0:
            break
        print('%d = %d + %d' % (n, a, b))
        continue
    break
