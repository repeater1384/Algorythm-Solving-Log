a,b = map(int,input().split())
if a>b:
    print(a-b)

else:
    queue = [(a,0)]
    visited = [0] * 100001
    while queue:
        cur,count = queue.pop(0)
        if cur == b:
            print(count)
            break
        if not visited[cur]:
            visited[cur] = 1
            if 0 <= cur - 1 <= 100000 and not visited[cur-1]:queue.append((cur-1,count+1))
            if 0 <= cur + 1 <= 100000 and not visited[cur+1]:queue.append((cur+1,count+1))
            if 0 <= cur * 2 <= 100000 and not visited[cur*2]:queue.append((cur*2,count+1))
