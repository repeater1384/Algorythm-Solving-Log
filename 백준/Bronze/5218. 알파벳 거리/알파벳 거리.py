for _ in range(int(input())):
    k=[]
    for a,b in zip(*input().split()):
        z=ord(b)-ord(a)
        k.append(z if z>=0 else z+26)
    print('Distances:',*k)