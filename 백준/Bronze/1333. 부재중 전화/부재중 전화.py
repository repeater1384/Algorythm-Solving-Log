N, L, D = map(int, input().split())
arr = []
for i in range(N):
    arr.extend([0] * L + [1] * 5)
arr.extend([1] * (N * L * D))
for i in range(D, len(arr), D):
    if arr[i] == 1:
        print(i)
        break
