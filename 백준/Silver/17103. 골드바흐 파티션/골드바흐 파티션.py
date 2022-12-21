is_prime = [True] * 1_000_000
primes = []
for i in range(2, len(is_prime)):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, len(is_prime), i):
            is_prime[j] = False

for _ in range(int(input())):
    target = int(input())
    cnt = 0
    for a in primes:
        b = target - a
        if a > b:
            break
        s, e = 0, len(primes) - 1
        while s <= e:
            m = (s + e) // 2
            if primes[m] == b:
                cnt += 1
                break
            elif primes[m] > b:
                e = m - 1
            else:
                s = m + 1
    print(cnt)
