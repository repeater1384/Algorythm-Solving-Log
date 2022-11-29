import sys
input = sys.stdin.readline

def dfs(prev, cur):
    visited[cur] = True
    for next in adj_list[cur]:
        if next == prev:
            continue
        if visited[next]:
            return False
        if not dfs(cur, next):
            return False
    return True

tc = 1
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    visited = [False] * (N + 1)
    answer = 0
    for i in range(1, N + 1):
        if not visited[i]:
            if dfs(-1, i):
                answer += 1
    if answer == 0:
        print(f'Case {tc}: No trees.')
    elif answer == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {answer} trees.')
    tc += 1

