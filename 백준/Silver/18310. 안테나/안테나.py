N = int(input())
arr = [*map(int, input().split())]
arr.sort()
print(arr[(N - 1) // 2])
