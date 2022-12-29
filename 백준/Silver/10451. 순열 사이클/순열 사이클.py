def dfs(cur):
    visited[cur] = True
    if not visited[arr[cur]]:
        dfs(arr[cur])


T = int(input())
for _ in range(T):
    N = int(input())
    arr = [*map(lambda x: int(x) - 1, input().split())]
    visited = [False] * N
    answer = 0
    for i in range(N):
        if not visited[i]:
            answer += 1
            dfs(i)
    print(answer)
