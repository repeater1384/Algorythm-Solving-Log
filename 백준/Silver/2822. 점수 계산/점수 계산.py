a=sorted([(int(input()),i+1)for i in range(8)])[3:]
k=1
for i in zip(*a):
    if k:print(sum(i));k-=1
    else:print(*sorted(i))