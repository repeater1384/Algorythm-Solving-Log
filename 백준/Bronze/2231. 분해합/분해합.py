def Decomposition(N):

    decomposition = int(N)

    a = list(map(int,list(N)))

    for i in a:
        decomposition += i

    return decomposition

N = int(input()) #정답

for i in range(0,N+1):
    if(Decomposition(str(i))==N):print(i);break
else:
    print(0)
