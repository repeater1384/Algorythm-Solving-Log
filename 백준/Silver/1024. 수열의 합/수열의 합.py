N, L = map(int, input().split())

for l in range(L, 101):
    lx = N - (l * (l + 1) // 2)
    if lx % l == 0:
        x = lx // l
        if x + 1 >= 0:
            print(*(i for i in range(x + 1, x + l + 1)))
            break
else:
    print(-1)