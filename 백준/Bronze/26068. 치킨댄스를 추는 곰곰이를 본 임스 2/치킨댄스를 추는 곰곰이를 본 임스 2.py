N = int(input())
answer = 0
for _ in range(N):
    _, n = input().split('-')
    if int(n) <= 90:
        answer += 1
print(answer)
