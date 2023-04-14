a,b=map(int,input().split())
if a>=b and int((a+b)/2) == (a+b)/2 and int((a-b)/2) == (a-b)/2:
    print((a+b)//2,(a-b)//2)
else:print(-1)