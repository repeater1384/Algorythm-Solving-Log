n=int(input())

for i in range(1,n+1):
    if i != n:
        print(' '*(n-i-1),end='')
        print(' *'*i,end='')
        print()
    else:
        print('* '*i)