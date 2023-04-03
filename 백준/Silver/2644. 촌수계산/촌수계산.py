#DFS

n = int(input())
a, b = map(int, input().split())
matrix = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(int(input())):
    x, y = map(int, input().split())
    matrix[y][x] = True
    matrix[x][y] = True


def dfs(cur_node, target_node, depth):
    if cur_node == target_node:
        print(depth)
        exit()

    visited[cur_node] = True

    for i in range(1, n + 1):
        if matrix[cur_node][i] and not visited[i]:
            dfs(i, target_node, depth + 1)

dfs(a, b, 0)
print(-1)