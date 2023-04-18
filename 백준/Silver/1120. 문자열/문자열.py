def getDif(a,b):
    dif = 0
    for i,j in zip(a,b):
        if i!=j:dif+=1
    return dif

a,b = input().split()
answer = len(b)
for i in range(len(b)-len(a)+1):
    j = len(b)-len(a) - i
    if j>0:temp = b[:i]+a+b[-j:]
    else:temp = b[:i] + a
    if getDif(temp,b) < answer:answer = getDif(temp,b)
print(answer)