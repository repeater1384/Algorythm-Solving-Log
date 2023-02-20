import sys

iuput = sys.stdin.readline
sys.setrecursionlimit(10 ** 6 + 10)


def find(x):
    global parents
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def is_same_parent(a, b):
    return find(a) == find(b)


def union(a, b):
    global parents
    a, b = find(a), find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


N, Q = map(int, input().split())

tree = []
for i in range(N):
    x1, x2, _ = map(int, input().split())
    tree.append((x1, x2, i))
tree.sort()

parents = [i for i in range(N)]
start_x, end_x, idx = tree[0]
for i in range(1, N):
    next_start_x, next_end_x, next_idx = tree[i]

    # 아예 안겹칠때
    if end_x < next_start_x:
        start_x = next_start_x
        end_x = next_end_x
        idx = next_idx
    # 겹칠때. 유니온.
    else:
        # 끝길이 늘려놓기.
        end_x = max(end_x, next_end_x)
        union(idx, next_idx)

answer = []
for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, input().split())
    answer.append(int(is_same_parent(a, b)))
print(*answer, sep='\n')

