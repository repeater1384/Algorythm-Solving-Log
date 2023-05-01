def get_all_true_factor(num):
    _true_factor = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            _true_factor.add(i)
            _true_factor.add(num // i)

    return sorted(_true_factor - {num})


while True:
    n = int(input())
    
    if n == -1:
        break

    true_factor = get_all_true_factor(n)

    if sum(true_factor) == n:
        print(f"{n} = {' + '.join(map(str, true_factor))}")
    else:
        print(f'{n} is NOT perfect.')
