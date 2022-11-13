import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6
                      )
N, M, R = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
for i in range(N + 1):
    adj_list[i].sort()
answer = [0] * (N + 1)
order = 1


def dfs(cur):
    global order
    answer[cur] = order
    order += 1
    for next in adj_list[cur]:
        if answer[next] == 0:
            dfs(next)


dfs(R)
print(*answer[1:], sep='\n')
