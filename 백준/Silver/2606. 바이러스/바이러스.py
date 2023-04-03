edges = {}
for i in range(int(input())):
    edges[i+1] = []

for _ in range(int(input())):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

stack = [1]
visited = []
while stack:
    cur = stack.pop()
    if cur not in visited:
        visited.append(cur)
        for item in edges[cur]:
            stack.append(item)

print(len(visited)-1)