n=int(input())
m=int(input())
k=input()
answer = 0
pn = 'IO'*n+'I'
for i in range(len(k)-len(pn)+1):
    if k[i:i+len(pn)] == pn:
        answer += 1
print(answer)