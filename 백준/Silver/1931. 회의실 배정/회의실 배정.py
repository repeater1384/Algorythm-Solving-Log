h = sorted(sorted([list(map(int,input().split(' '))) for _ in range(int(input()))],key= lambda x:x[0]),key = lambda x:x[1])
answer = 0
cur = 0

for i in h:
    if cur <= i[0]:
        cur = i[1]
        answer += 1
        
print(answer)

