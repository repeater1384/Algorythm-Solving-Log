l=[0,1,1,1,2,2]
for i in range(6,101):l.append(l[i-1]+l[i-5])
eval('print(l[int(input())]),'*int(input()))