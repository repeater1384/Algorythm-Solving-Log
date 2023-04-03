f = [-1] * 51
n = int(input())
def fibo(n):
    if n<2:
        f[n] = 1
        return f[n]
    else:
        if f[n] == -1:
            f[n] = 1 + fibo(n-1) + fibo(n-2)
        return f[n]
# def fibo2(n):
#     if n<2:
#         return 1
#     else:
#         return 1+fibo2(n-1)+fibo2(n-2)

print(fibo(n)%1000000007 )
