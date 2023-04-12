arr = set(int(input()) for _ in range(int(input())))

answer = float('inf')
for a in arr:
    for i in range(-4, 1):
        target = set(a + i + k for k in range(5))
        answer = min(answer, len(target - arr))
print(answer)
