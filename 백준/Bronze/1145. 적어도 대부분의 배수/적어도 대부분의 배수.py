numbers = [*map(int, input().split())]

answer = 1
while True:
    count = 0
    for i in range(5):
        if answer % numbers[i] == 0:
            count += 1
    if count >= 3:
        print(answer)
        break
    answer += 1
    
