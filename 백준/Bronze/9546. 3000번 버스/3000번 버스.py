for _ in range(int(input())):
    k = int(input())
    n = 0
    while k:
        n = n * 2 + 1
        k -= 1
    print(n)
