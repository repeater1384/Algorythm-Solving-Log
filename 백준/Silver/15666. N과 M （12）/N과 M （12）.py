def create():
    if len(temp) == M:
        print(*temp)
        return

    for i in range(len(arr)):
        if not temp or temp[-1] <= arr[i]:
            temp.append(arr[i])
            create()
            temp.pop()


N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
temp = []

create()
