import sys
import math

MAX_N = 10 ** 5
sys.setrecursionlimit(MAX_N+1)
input = sys.stdin.readline

N = int(input())
LOG = int(math.log2(MAX_N)) + 1
adj_list = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, weight = map(int, input().split())
    adj_list[a].append((b, weight))
    adj_list[b].append((a, weight))

depth = [-1] * (N + 1)
parents = [[-1] * LOG for _ in range(N + 1)]
cost = [[0] * LOG for _ in range(N + 1)]


def dfs(cur, d):
    depth[cur] = d
    for next, weight in adj_list[cur]:
        if depth[next] == -1:
            cost[next][0] = weight
            parents[next][0] = cur
            dfs(next, d + 1)


# 2^0 번째 조상 세팅, 1번 노드를 루트로.
dfs(1, 0)

# 2^i 번째 조상 세팅
for i in range(1, LOG):
    for j in range(1, N + 1):
        parents[j][i] = parents[parents[j][i - 1]][i - 1]
        cost[j][i] = cost[j][i - 1] + cost[parents[j][i - 1]][i - 1]


# a에서 b까지 비용 구하기
def query1(a, b):
    total_cost = 0

    if depth[a] > depth[b]:
        a, b = b, a

    need = depth[b] - depth[a]
    for i in range(LOG - 1, -1, -1):
        if need & (1 << i):
            total_cost += cost[b][i]
            b = parents[b][i]
    if a == b:
        return total_cost
    for i in range(LOG - 1, -1, -1):
        # 의심스러움 ㅋ
        if parents[a][i] != parents[b][i]:
            total_cost += cost[a][i] + cost[b][i]
            a = parents[a][i]
            b = parents[b][i]

    return total_cost + cost[a][0] + cost[b][0]


def query2(a, b, k):
    first_a, first_b = a, b
    a_distance, b_distance = 0, 0
    need = abs(depth[b] - depth[a])

    if depth[b] > depth[a]:
        for i in range(LOG - 1, -1, -1):
            if need & (1 << i):
                b = parents[b][i]
                b_distance += 1 << i
    else:
        for i in range(LOG - 1, -1, -1):
            if need & (1 << i):
                a = parents[a][i]
                a_distance += 1 << i
    if a == b:
        # LCA가 a,b 중 하나인 경우
        if depth[first_a] < depth[first_b]:
            k = depth[first_b] - depth[first_a] - k
            for i in range(LOG - 1, -1, -1):
                if k & (1 << i):
                    first_b = parents[first_b][i]
            return first_b
        else:
            for i in range(LOG - 1, -1, -1):
                if k & (1 << i):
                    first_a = parents[first_a][i]
            return first_a

    for i in range(LOG - 1, -1, -1):
        if parents[a][i] != parents[b][i]:
            a = parents[a][i]
            b = parents[b][i]
            a_distance += 1 << i
            b_distance += 1 << i
    a_distance += 1
    b_distance += 1

    if a_distance >= k:
        for i in range(LOG - 1, -1, -1):
            if k & (1 << i):
                first_a = parents[first_a][i]
        return first_a
    else:
        k = a_distance + b_distance - k
        for i in range(LOG - 1, -1, -1):
            if k & (1 << i):
                first_b = parents[first_b][i]
        return first_b


answer = []
K = int(input())
for _ in range(K):
    query_no, *queries = map(int, input().split())
    if query_no == 1:
        a, b = queries
        answer.append(query1(a, b))
    elif query_no == 2:
        a, b, k = queries
        answer.append(query2(a, b, k - 1))

print(*answer, sep='\n')
