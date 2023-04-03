arr=[input() for _ in range(5)]
maxlen=0
for i in arr:
    if maxlen < len(i):
        maxlen = len(i)
for i in range(len(arr)):
    arr[i] = arr[i]+ ' '*(maxlen-len(arr[i]))
for i in zip(*arr):
    print(''.join(i).replace(' ',''),end='')