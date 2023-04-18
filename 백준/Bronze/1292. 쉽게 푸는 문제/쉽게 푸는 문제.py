a,b=map(int,input().split());k=[]
for i in range(1,46):k+=[i]*i
print(sum(k[:b])-sum(k[:a-1]))