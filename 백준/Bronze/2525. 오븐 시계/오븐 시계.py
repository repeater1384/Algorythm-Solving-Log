i=input
a,b=map(int,i().split())
c=int(i())
k=a*60+b+c
print(k//60%24,k%60)