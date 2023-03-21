import sys
import math

MAX_N = 10 ** 5
sys.setrecursionlimit(MAX_N)
input = sys.stdin.readline
INF = float('inf')

N = int(input())
LOG = int(math.log2(MAX_N)) + 1
adj_list = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, weight = map(int, input().split())
    adj_list[a].append((b, weight))
    adj_list[b].append((a, weight))

depth = [-1] * (N + 1)
parents = [[-1] * LOG for _ in range(N + 1)]
max_distance = [[-INF] * LOG for _ in range(N + 1)]
min_distance = [[INF] * LOG for _ in range(N + 1)]


def dfs(cur, d):
    depth[cur] = d
    for next, weight in adj_list[cur]:
        if depth[next] == -1:
            max_distance[next][0] = weight
            min_distance[next][0] = weight
            parents[next][0] = cur
            dfs(next, d + 1)


# 2^0 번째 조상 세팅, 1번 노드를 루트로.
dfs(1, 0)

# 2^i 번째 조상 세팅
for i in range(1, LOG):
    for j in range(1, N + 1):
        parents[j][i] = parents[parents[j][i - 1]][i - 1]
        min_distance[j][i] = min(min_distance[j][i - 1], min_distance[parents[j][i - 1]][i - 1])
        max_distance[j][i] = max(max_distance[j][i - 1], max_distance[parents[j][i - 1]][i - 1])


def query(a, b):
    min_dis, max_dis = INF, -INF
    # b가 더 깊이 있도록
    if depth[a] > depth[b]:
        a, b = b, a

    # need = b가 거슬러 올라와야 하는 양
    need = depth[b] - depth[a]
    for i in range(LOG - 1, -1, -1):
        if need & (1 << i):
            min_dis = min(min_dis, min_distance[b][i])
            max_dis = max(max_dis, max_distance[b][i])
            b = parents[b][i]
            # need -= 1 << i
    # 이미 같은 노드에 있다면.
    if a == b:
        return min_dis, max_dis
    # 한칸 직전까지 올려줌
    for i in range(LOG - 1, -1, -1):
        if parents[a][i] != parents[b][i]:
            min_dis = min(min_dis, min_distance[a][i], min_distance[b][i])
            max_dis = max(max_dis, max_distance[a][i], max_distance[b][i])
            a = parents[a][i]
            b = parents[b][i]

    min_dis = min(min_dis, min_distance[a][0], min_distance[b][0])
    max_dis = max(max_dis, max_distance[a][0], max_distance[b][0])
    return min_dis, max_dis


answer = []
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    min_dis, max_dis = query(a, b)
    answer.append(f'{min_dis} {max_dis}')

print(*answer, sep='\n')
