def fast_pow(a, b):
    # calc a^b fast!!
    if b == 0:
        return 1
    temp = fast_pow(a, b // 2)
    if b % 2 == 1:
        return temp * temp * a % MOD
    return temp * temp % MOD


N = int(input())
arr = sorted(map(int, input().split()))
MOD = 1_000_000_007
answer = 0
for i, num in enumerate(arr):
    # num이 최소가 되는 집합의 개수
    max_set_n = fast_pow(2, i) % MOD
    # num이 최대가 되는 집합의 개수
    min_set_n = fast_pow(2, N - 1 - i) % MOD
    answer = (answer + (max_set_n * num % MOD) - (min_set_n * num % MOD)) % MOD

print(answer)
