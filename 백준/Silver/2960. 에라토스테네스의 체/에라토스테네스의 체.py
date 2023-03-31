N,K=map(int,input().split())
arr = [*range(2,N+1)]
deleted = []
while len(deleted) < K:
    a = arr.pop(0)
    deleted.append(a)
    for i in arr:
        if i%a == 0:
            deleted.append(arr.pop(arr.index(i)))
print(deleted[K-1])
