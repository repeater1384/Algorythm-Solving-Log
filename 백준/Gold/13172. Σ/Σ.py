from functools import reduce

MOD = 1_000_000_007

M = int(input())
answer = []
for _ in range(M):
    n, s = map(int, input().split())
    answer.append((s * pow(n, MOD - 2, MOD)) % MOD)

print(reduce(lambda x, y: (x + y) % MOD, answer))
