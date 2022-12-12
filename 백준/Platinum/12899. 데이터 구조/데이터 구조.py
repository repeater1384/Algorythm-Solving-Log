import sys

input = sys.stdin.readline


class SegmentTree:
    def __init__(self, arr, N):
        self.arr = arr
        self.tree = [0] * (N * 4)

    def query(self, node, start, end, rank):
        # rank번째 node를 구하고, 거쳐온 노드들 -1 하기
        self.tree[node] -= 1
        if start == end:
            return start
        mid = (start + end) // 2
        left = self.tree[node * 2]
        if left >= rank:
            return self.query(node * 2, start, mid, rank)
        else:
            return self.query(node * 2 + 1, mid + 1, end, rank - left)

    def update(self, node, start, end, idx):
        # idx까지 내려가면서 거쳐온 노드들 + 1 하기
        if end < idx or idx < start:
            return
        self.tree[node] += 1
        if start == end:
            return
        mid = (start + end) // 2
        self.update(node * 2, start, mid, idx)
        self.update(node * 2 + 1, mid + 1, end, idx)


T = int(input())

N = 2_000_000 + 1
tree = SegmentTree([0] * N, N)
answer = []
for _ in range(T):
    q, n = map(int, input().split())
    if q == 1:
        tree.update(1, 1, N, n)
    if q == 2:
        num = tree.query(1, 1, N, n)
        answer.append(num)
print(*answer, sep='\n')
