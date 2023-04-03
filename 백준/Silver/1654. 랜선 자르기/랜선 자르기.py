k,n = map(int,input().split())
lan = [int(input()) for _ in range(k)]
start,end = 1,max(lan)

while start <= end:
    mid = (start+end)//2
    cur = sum(map(lambda x:x//mid,lan))
    if cur < n:
        end = mid - 1
    else:
        start = mid + 1
print(end)