arr = [*map(int, input().split())]
x, _, _ = map(int, input().split())
print(arr.index(x) + 1 if x in arr else 0)
