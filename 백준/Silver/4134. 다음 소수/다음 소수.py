def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    N = int(input())
    while True:
        if is_prime(N):
            print(N)
            break
        N += 1
