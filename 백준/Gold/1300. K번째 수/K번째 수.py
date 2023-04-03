n,k=eval('int(input()),'*2)
a=s=0
e=k
while s<=e:
    m=(s+e)//2
    s,e,a=(s,m-1,m)if k<=sum(min(n,m//i)for i in range(1,n+1))else(m+1,e,a)
print(a)