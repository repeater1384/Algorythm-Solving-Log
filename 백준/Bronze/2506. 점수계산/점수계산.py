input()
list = list(map(int,input().split())) + [0]
countlist = []
i = 0
for n in list:
    if n==1:
        i+=1
    else:
        countlist.append(i)
        i=0
print(sum(map(lambda x:x*(x+1)//2,countlist)))