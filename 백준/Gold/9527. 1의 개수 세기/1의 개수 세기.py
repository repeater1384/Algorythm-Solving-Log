A, B = map(int, input().split())
table = [0] * 66

for i in range(1, 66):
    table[i] = table[i - 1] * 2 + (1 << (i - 1))


def get_one_count(N):
    cnt = 0
    while N > 0:
        log = len(bin(N)) - bin(N).index('1') - 1
        cnt += table[log]
        N -= 2 ** log
        cnt += N + 1
    return cnt


print(get_one_count(B) - get_one_count(A - 1))
