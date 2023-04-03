c,a,b=map(int,input().split())
k = c/((a*a+b*b)**0.5)
print(int(a*k),int(b*k))