a=[*map(int,input().split())]
b=[1,1,2,2,2,8]
for a,b in zip(a,b):print(b-a,end=' ')