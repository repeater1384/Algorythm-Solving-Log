n,k = map(int,input().split())
for i in range(1,n+1):
    if n%i == 0:k-=1
    if not k:
        print(i)
        break
else:
    print(0)