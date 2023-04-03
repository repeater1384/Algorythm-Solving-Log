a,y,b = eval('input(),'*3)
if y=='*':
    print('1'+'0'*(len(a+b)-2))
else:
    if a==b:
        print('2'+'0'*(len(a)-1))
    else:
        if a<b:
            a,b = b,a
        print('1'+'0'*(len(a)-len(b)-1)+'1'+'0'*(len(b)-1))
