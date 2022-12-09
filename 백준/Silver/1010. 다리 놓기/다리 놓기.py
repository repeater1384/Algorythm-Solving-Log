def fac(n):
    a=1
    while n:
        a*=n
        n-=1
    return a
for _ in range(int(input())):
    n,m = map(int,input().split())
    print(fac(m)//fac(n)//fac(m-n))