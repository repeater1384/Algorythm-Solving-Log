N = int(input())
arr = [*map(int, input().split())]

result = set()
for bit in range(1, 1 << N):
    cur = 0
    for i in range(N):
        if bit & (1 << i):
            cur += arr[i]
    result.add(cur)

num = 1
while True:
    if num in result:
        num += 1
    else:
        print(num)
        break
