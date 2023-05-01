N = int(input())

adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def dfs():  # 1 제외 모든 노드의 부모 노드 리스트를 반환
    stack = [1]
    visited = [0] * (N + 1)
    parents = [None] * (N + 1)
    while stack:
        cur = stack.pop()
        visited[cur] = 1

        for i in adj[cur]:
            if not visited[i]:
                stack.append(i)
                parents[i] = cur

    return parents


print(*dfs()[2:], sep='\n')
