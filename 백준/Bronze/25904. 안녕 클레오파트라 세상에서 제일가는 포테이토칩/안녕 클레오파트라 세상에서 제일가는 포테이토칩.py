N, X = map(int, input().split())
arr = [*map(int, input().split())]

idx = 0
while True:
    if arr[idx] < X:
        print(idx + 1)
        break
    idx = (idx + 1) % N
    X += 1
