for _ in range(int(input())):
    p,m = map(int,input().split())
    cantsit = 0
    l = {i+1:True for i in range(m)}
    for _ in range(p):
        sit = int(input())
        if l[sit]:l[sit]=False
        else:cantsit += 1
    print(cantsit)