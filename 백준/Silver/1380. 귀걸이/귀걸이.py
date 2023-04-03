case = 1
while True:
    n = int(input())
    if n == 0: break

    names = [""] + [input() for _ in range(n)]
    check = [2] * (n + 1)
    for _ in range(2 * n - 1):
        num, _ = input().split()
        check[int(num)] -= 1

    for num in range(1, n + 1):
        if check[num]:
            print(f'{case} {names[num]}')
    case += 1
