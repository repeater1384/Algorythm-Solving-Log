for _ in range(int(input())):
    n,m = map(int,input().split())
    que = [*map(int,input().split())]
    seq = [i for i in range(len(que))]
    newque = [*zip(que,seq)]
    cnt = 0
    while True:
        maxval =max(newque,key = lambda x :x[0])[0]
        cur = newque.pop(0)
        if cur[0] >= maxval:
            cnt+=1
            if cur[1] == m:
                print(cnt)
                break
        else:
            newque.append(cur)