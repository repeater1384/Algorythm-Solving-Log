n,m=map(int,input().split())
print(max(m//2*n+m%2*n//2,n//2*m+n%2*m//2))