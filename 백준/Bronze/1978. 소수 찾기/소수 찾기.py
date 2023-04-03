n = int(input())
numbers = [*map(int, input().split())]
answer = 0

for num in numbers:
    if num <= 1:
        continue

    condition = True
    for i in range(2, num):
        if num % i == 0:
            condition = False
            break
    if condition:
        answer += 1
        
print(answer)