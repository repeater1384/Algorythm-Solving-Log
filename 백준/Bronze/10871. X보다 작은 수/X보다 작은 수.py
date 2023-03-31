N,X = map(int,input().split(' '))
for k in [i for i in list(map(int,input().split(' '))) if i<X]:print(k,end=' ')