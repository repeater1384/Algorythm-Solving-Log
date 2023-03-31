import sys

input = sys.stdin.readline
sys.setrecursionlimit(500000)
N = int(input())
adj_list = [[] for _ in range(1 + N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [False] * (N + 1)
cnt = 0


def dfs(depth, cur):
    global cnt
    visited[cur] = True
    if not adj_list[cur]:
        cnt += depth
        return
    is_leaf = True
    for next in adj_list[cur]:
        if not visited[next]:
            dfs(depth + 1, next)
            is_leaf = False
    if is_leaf:
        cnt += depth


dfs(0, 1)
print('Yes' if cnt % 2 else 'No')
