n = int(input())

if n == 1:print(1)
else:
    start,end = 2, 7
    count = 1
    while True:
        if start<=n<=end:
            print(count+1)
            break
        else:
            start = end+1
            end += (count+1) * 6
            count+=1
