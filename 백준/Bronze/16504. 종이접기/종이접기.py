answer = 0
for _ in range(int(input())):
    answer += sum(map(int,input().split(' ')))
print(answer)