def fac(num):
    if num == 1: return 1
    return num * fac(num - 1)


n, m = map(int, input().split())

print(fac(n)//(fac(m)*fac(n-m)))
