arr = set([int(input()) for _ in range(int(input()))])

answer = float('inf')
for a in arr:
    for i in range(-4, 1):
        temp = 0
        for k in range(5):
            if a + i + k not in arr:
                temp += 1
        answer = min(answer, temp)
print(answer)
