X = int(input())


def get_scope(x):
    for n in range(1, x + 1):
        if n * (n + 1) // 2 >= x:
            return n


scope = get_scope(X)
start = scope * (scope - 1) // 2
hmtimes = X - start - 1
if scope % 2:
    bunza, bunmo = scope - hmtimes, 1 + hmtimes
else:
    bunza, bunmo = 1 + hmtimes, scope - hmtimes

print(f'{bunza}/{bunmo}')
