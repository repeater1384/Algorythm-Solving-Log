for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if b-c > a:
        print('advertise')
    elif b-c<a:
        print('do not advertise')
    else:
        print('does not matter')