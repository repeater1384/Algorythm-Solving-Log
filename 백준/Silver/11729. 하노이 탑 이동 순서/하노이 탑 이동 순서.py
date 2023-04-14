def hanoi(n,start,temp,end):
    if n == 1:
        print(start,end)
    else:
        hanoi(n-1,start,end,temp)
        hanoi(1,start,temp,end)
        hanoi(n-1,temp,start,end)
    return
n = int(input())
print(pow(2,n)-1)
hanoi(n,1,2,3)