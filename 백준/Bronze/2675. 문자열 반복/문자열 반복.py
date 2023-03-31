T = int(input())
for _ in range(T):
    count, words = input().split()
    count = int(count)

    for w in words:
        print(w * count, end='')
    print()