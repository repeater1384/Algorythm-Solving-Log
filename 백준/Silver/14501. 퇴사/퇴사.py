N = int(input())
work_pay = []
max_pay = [0] * N

for _ in range(N):
    work_pay.append(list(map(int, input().split())))

for i in range(N-1,-1,-1):

    day = work_pay[i][0]
    pay = work_pay[i][1]


    if i + day > N:
        if i != N-1:
            max_pay[i] = max_pay[i+1]
    elif i == N-1:
        max_pay[i] = pay

    if i + day == N and i != N-1:
        max_pay[i] = max(pay,max_pay[i+1])

    if i + day < N:
        max_pay[i] = max(pay+max_pay[i+day],max_pay[i+1])

print(max_pay[0])