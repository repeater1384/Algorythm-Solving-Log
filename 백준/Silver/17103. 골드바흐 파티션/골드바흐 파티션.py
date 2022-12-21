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
        if is_prime[b]:
            cnt += 1
    print(cnt)
