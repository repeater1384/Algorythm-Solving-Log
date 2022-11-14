N = int(input())
tree = [*map(int, input().split())]
remove_node = int(input())


def dfs(_remove_node):
    tree[_remove_node] = -2
    for node in range(len(tree)):
        parent = tree[node]
        if parent == _remove_node:
            dfs(node)


dfs(remove_node)

count = 0
for node in range(len(tree)):
    if tree[node] != -2 and node not in tree:
        count += 1
print(count)
