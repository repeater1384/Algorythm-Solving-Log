def fac(n):
    if n <= 1: return 1
    return n * fac(n - 1)


def comb(n, m):
    return fac(n) // (fac(m) * fac(n - m))


N, M, K = map(int, input().split())

answer = 0
for i in range(K, M + 1):
    answer += comb(M, i) * comb(N - M, M - i)
print(answer / comb(N,M))
