n,m = map(int,input().split())
check = [False] *(n+1)
answer =[0] * m

def recucive(index,n,m,start):
    if index == m:
        for i in range(m):
            print(answer[i],end=' ')
        print()
        return

    for i in range(start,n+1):
        if check[i]:
            continue

        check[i] = True
        answer[index] = i
        recucive(index+1,n,m,i+1)
        check[i] = False

recucive(0,n,m,1)