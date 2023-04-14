import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, S, E = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, dis = map(int, input().split())
    adj_list[a].append((b, dis))
    adj_list[b].append((a, dis))

visited = [False] * (N + 1)


def dfs(cur, dis_sum, max_dis):
    global answer
    if cur == E:
        print(dis_sum - max_dis)
        return
    for next, dis in adj_list[cur]:
        if not visited[next]:
            visited[cur] = True
            dfs(next, dis_sum + dis, max(max_dis, dis))
            visited[cur] = False


dfs(S, 0, 0)
