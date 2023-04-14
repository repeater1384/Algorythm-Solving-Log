def create():
    if len(temp) == M:
        print(*temp)
        return
    previous = 0

    for i in range(N):
        if not visited[i] and arr[i] != previous:
            visited[i] = True
            temp.append(arr[i])
            previous = arr[i]
            create()
            temp.pop()
            visited[i] = False


N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [False] * (N + 1)
temp = []

create()
