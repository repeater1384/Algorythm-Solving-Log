def dfs(cur, cnt):
    if cnt == 4:
        return True
    for next in adj_list[cur]:
        if not visited[next]:
            visited[next] = True
            res = dfs(next, cnt + 1)
            if res:
                return True
            visited[next] = False
    return False


N, M = map(int, input().split())
adj_list = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(N):
    visited = [False] * N
    visited[i] = True
    if dfs(i, 0):
        print(1)
        break
else:
    print(0)
