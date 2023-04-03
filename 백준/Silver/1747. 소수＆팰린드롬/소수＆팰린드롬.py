N = int(input())


def make_primes(size):
    _primes = [False, False] + [True] * (size - 1)

    for i in range(2, size + 1):
        if _primes[i]:
            for j in range(i + i, size + 1, i):
                _primes[j] = False

    return _primes


def check_penlildrome(num):
    return str(num) == str(num)[::-1]


primes = make_primes(1003002)
for i in range(N, 1003002):
    if primes[i] and check_penlildrome(i):
        print(i)
        break
