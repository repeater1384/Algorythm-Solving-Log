def combination(arr,r):
    def generation(choose):
        if len(choose)  == r:
            print(*choose)
            return
        else:
            start = arr.index(choose[-1]) + 1 if choose else 0
            for i in range(start,len(arr)):
                choose.append(arr[i])
                generation(choose)
                choose.pop()
    generation([])
while True:
    k = list(map(int,input().split()))
    if k[-1] == 0:break
    combination(k[1:],6)
    print()