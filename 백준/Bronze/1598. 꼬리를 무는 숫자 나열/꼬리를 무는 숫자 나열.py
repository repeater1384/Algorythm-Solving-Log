n,m = map(lambda x : int(x)-1 ,input().split())
garo = abs(n//4 - m//4)
sero = abs(n%4-m%4)
print(garo+sero)