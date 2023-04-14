def find(x):
    global parents
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    global parents
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


N = int(input())
distance = [[float('inf')] * N for _ in range(N)]
parents = [i for i in range(N)]
for _ in range(int(input())):
    x, y = map(lambda i: int(i) - 1, input().split())
    distance[x][y] = distance[y][x] = 1
    union(x, y)

for k in range(N):
    distance[k][k] = 0
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

representative = {}
for i in range(N):
    root = find(i)
    deliver_time = max([dis for dis in distance[i] if dis != float('inf')])
    if root in representative:
        prev_i, prev_deliver_time = representative[root]
        if deliver_time < prev_deliver_time:
            representative[root] = (i, deliver_time)
    else:
        representative[root] = (i, deliver_time)

print(len(representative))
print(*map(lambda x: x[0] + 1, sorted(representative.values(), key=lambda y: y[0])), sep='\n')
