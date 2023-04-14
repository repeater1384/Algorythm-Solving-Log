N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
INF = float('inf')
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))


def dfs(cur, end, cost):
    if cur == end:
        return cost
    visited[cur] = True
    answer = INF
    for next, next_cost in adj_list[cur]:
        if not visited[next]:
            answer = min(answer, dfs(next, end, cost + next_cost))
    return answer


for _ in range(M):
    a, b = map(int, input().split())
    visited = [False] * (N + 1)
    print(dfs(a, b, 0))
