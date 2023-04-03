for _ in range(int(input())):
    n, k = map(int, input().split())
    candies = [*map(int, input().split())]
    print(sum([candy // k for candy in candies]))
