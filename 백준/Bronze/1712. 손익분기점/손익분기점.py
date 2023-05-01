a,b,c = map(int,input().split())
if(c<=b):
    print(-1)
else:
    print(int(a/(c-b))+1)