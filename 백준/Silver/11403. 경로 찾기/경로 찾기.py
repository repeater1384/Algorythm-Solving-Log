N = int(input())
matrix = [[*map(int, input().split())] for _ in range(N)]


def dfs(start):
    queue = [start]
    visited = [0] * N

    while queue:
        cur = queue.pop(0)
        for idx, v in enumerate(matrix[cur]):
            if v and visited[idx] == 0:
                queue.append(idx)
                visited[idx] = 1

    return visited


for i in range(N):
    print(*dfs(i))
