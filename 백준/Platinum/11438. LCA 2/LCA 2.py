import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
LOG = 21
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

depth = [-1] * (N + 1)
visited = [False] * (N + 1)
parents = [[-1] * LOG for _ in range(N + 1)]


def dfs(cur, d):
    visited[cur] = True
    depth[cur] = d
    for next in adj_list[cur]:
        if visited[next]:
            continue
        parents[next][0] = cur
        dfs(next, d + 1)


def set_parents():
    # 2^0 번째 조상 세팅
    dfs(1, 0)

    # 2^i 번째 조상 세팅
    for i in range(1, LOG):
        for j in range(1, N + 1):
            parents[j][i] = parents[parents[j][i - 1]][i - 1]


set_parents()


def lca(a, b):
    # b가 더 깊이 있도록
    if depth[a] > depth[b]:
        a, b = b, a

    # b가 거슬러 올라와야 하는 양
    need = depth[b] - depth[a]
    for i in range(LOG - 1, -1, -1):
        if need >= (1 << i):
            b = parents[b][i]
            need -= 1 << i

    if a == b:
        return a

    for i in range(LOG - 1, -1, -1):
        if parents[a][i] != parents[b][i]:
            a = parents[a][i]
            b = parents[b][i]
    return parents[a][0]


answer = []
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    answer.append(lca(a, b))
print(*answer, sep='\n')
