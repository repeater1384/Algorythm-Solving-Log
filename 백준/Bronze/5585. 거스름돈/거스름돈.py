coin = [500,100,50,10,5,1]
all = 1000-int(input())
answer = 0
for c in coin:
    answer += all//c
    all%=c
print(answer)