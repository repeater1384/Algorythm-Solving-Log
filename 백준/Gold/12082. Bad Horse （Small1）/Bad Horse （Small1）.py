def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


def is_same_parents(x, y):
    return find(x) == find(y)


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    names = {}
    name_idx = 2
    relation = []
    for _ in range(N):
        a, b = input().split()
        if a not in names:
            names[a] = name_idx
            name_idx += 1
        if b not in names:
            names[b] = name_idx
            name_idx += 1
        relation.append(sorted((names[a], names[b])))
    parents = [i for i in range(name_idx)]
    relation.sort()
    can_split = True
    for a, b in relation:
        if is_same_parents(a, b):
            can_split = False
            break
        if find(a) == 0 or find(b) == 1:
            union(a, 0)
            union(b, 1)
        elif find(a) == 1 or find(b) == 0:
            union(a, 1)
            union(b, 0)
        else:
            union(a, 0)
            union(b, 1)
    print(f'Case #{case_num}: {"Yes" if can_split else "No"}')

