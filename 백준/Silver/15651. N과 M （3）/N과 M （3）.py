n,m = map(int,input().split())
answer =[0] * m

def recucive(index,n,m):
    if index == m:
        for i in range(m):
            print(answer[i],end=' ')
        print()
        return

    for i in range(1,n+1):
        answer[index] = i
        recucive(index+1,n,m)

recucive(0,n,m)