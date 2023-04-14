for _ in range(int(input())):
    print(sum([i * (i + 1) * (i + 2) // 2 for i in range(1, int(input()) + 1)]))
