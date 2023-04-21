def print_hanoi(start, mid, end, num):
    if num == 1:
        print(start, end)
        return

    print_hanoi(start, end, mid, num - 1)
    print(start, end)
    print_hanoi(mid, start, end, num - 1)


N = int(input())

print(2 ** N - 1)

if N <= 20:
    print_hanoi(1, 2, 3, N)
