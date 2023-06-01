N = int(input())
for _ in range(N):
    T, *arr = map(int, input().split())

    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1
        if freq[n] > T / 2:
            print(n)
            break
    else:
        print('SYJKGW')
