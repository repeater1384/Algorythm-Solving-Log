N = int(input())
M = int(input())
vip_seat = [int(input()) for _ in range(M)] + [N+1]

fibo = [1,1]
for _ in range(N):
    fibo.append(fibo[-1]+fibo[-2])

answer = 1
temp = 1
for i in vip_seat:
    answer *= fibo[i - temp]
    temp = i + 1
print(answer)