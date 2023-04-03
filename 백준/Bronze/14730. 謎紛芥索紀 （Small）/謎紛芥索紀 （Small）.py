answer = 0
for _ in range(int(input())):
    C, K = map(int, input().split())
    answer += C * K

print(answer)
