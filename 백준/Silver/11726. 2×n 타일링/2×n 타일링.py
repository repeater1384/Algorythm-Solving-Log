d=[0]*1001
def f(n):
    if n==1000:return 1115
    if d[n]==0:d[n]=n if n<3else f(n-1)+f(n-2)
    return d[n]
print(f(int(input()))%10007)