import sys

input = sys.stdin.readline
sys.setrecursionlimit(50000)
N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

depth = [-1] * (N + 1)
parents = [-1] * (N + 1)


def dfs(cur, _depth):
    depth[cur] = _depth
    for node in adj_list[cur]:
        if depth[node] == -1:
            dfs(node, _depth + 1)
            parents[node] = cur


dfs(1, 0)
M = int(input())
answer = []
for _ in range(M):
    a, b = map(int, input().split())
    # 항상 b가 더 깊도록.
    if depth[a] > depth[b]:
        a, b = b, a

    # 깊이 맞추기
    while depth[a] < depth[b]:
        b = parents[b]

    if a == b:
        answer.append(a)
        continue

    while a != b:
        a = parents[a]
        b = parents[b]
    answer.append(a)

print(*answer, sep='\n')
