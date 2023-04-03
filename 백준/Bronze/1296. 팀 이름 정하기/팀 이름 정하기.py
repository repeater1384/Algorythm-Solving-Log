name = input()
answer = []
for _ in range(int(input())):
    team = input()
    arr = [name.count(c)+team.count(c) for c in 'LOVE']
    temp = 1
    for i in range(3):
        for j in range(i+1,4):
            temp *= (arr[i]+arr[j])
    answer.append((temp%100,team))
answer.sort(key=lambda x:(-x[0],x[1]))
print(answer[0][1])
