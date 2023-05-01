def solution():
    L = int(input())
    arr = sorted(map(int, input().split()))
    n = int(input())
    prev = 0
    for num in arr:
        if num == n:
            return 0

        if num > n:
            min_val = prev + 1
            max_val = num - 1
            break
        prev = num

    return (n - min_val) * (max_val - n + 1) + (max_val - n)


print(solution())
