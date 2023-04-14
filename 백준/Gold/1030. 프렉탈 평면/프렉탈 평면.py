s, N, K, R1, R2, C1, C2 = map(int, input().split())


def is_black(y, x, size):
    if size == 1:
        return False
    grid = size // N
    start, end = ((N - K) // 2) * grid, ((N - K) // 2 + K) * grid
    if start <= y < end and start <= x < end:
        return True
    return is_black(y % grid, x % grid, grid)


answer = ''
for r in range(R1, R2 + 1):
    for c in range(C1, C2 + 1):
        answer += '1' if is_black(r, c, N ** s) else '0'
    answer += '\n'
print(answer)
