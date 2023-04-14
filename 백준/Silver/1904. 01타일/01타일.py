a = [1,2]*500001
c = 15746

def pibo(n):
    for i in range(2,n+1):
        a[i] = (a[i-1] % c + a[i-2]% c)%c
    return a[n-1]

print(pibo(int(input())))
