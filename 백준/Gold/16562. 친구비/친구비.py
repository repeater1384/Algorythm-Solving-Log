def find(x):
    global parents
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    global parents
    a, b = find(a), find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


N, M, K = map(int, input().split())
arr = [*map(int, input().split())]
parents = [i for i in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    union(a, b)

need_money = {}
for i in range(N):
    target = find(parents[i])
    if target not in need_money:
        need_money[target] = arr[i]
    else:
        need_money[target] = min(need_money[target], arr[i])

final_need_money = sum(need_money.values())
print(final_need_money if final_need_money <= K else 'Oh no')
