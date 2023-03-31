while 1:
    a,b=map(int,input().split())
    if not a+b:break
    print('Yes'if a>b else'No')