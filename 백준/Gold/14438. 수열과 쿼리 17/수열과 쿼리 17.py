import sys

input = sys.stdin.readline


class SegmentTree:
    def __init__(self, arr, N):
        self.arr = arr
        self.tree = [0] * (N * 4)
        self.init_tree(1, 1, N)

    def init_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            left = self.init_tree(node * 2, start, mid)
            right = self.init_tree(node * 2 + 1, mid + 1, end)
            self.tree[node] = min(left, right)
        return self.tree[node]

    def calc(self, node, start, end, left, right):
        # [left, right] 구간을 구함. left, right는 고정
        if right < start or end < left:
            return float('inf')
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2

        temp1 = self.calc(node * 2, start, mid, left, right)
        temp2 = self.calc(node * 2 + 1, mid + 1, end, left, right)
        return min(temp1, temp2)

    def update(self, node, start, end, new_idx, new_val):
        # new_idx의 값을 new_val로 바꿈, new_idx, new_val 고정
        if new_idx < start or end < new_idx:
            pass
        elif start == end:
            self.tree[node] = new_val
        else:
            mid = (start + end) // 2
            temp1 = self.update(node * 2, start, mid, new_idx, new_val)
            temp2 = self.update(node * 2 + 1, mid + 1, end, new_idx, new_val)
            self.tree[node] = min(temp1, temp2)
        return self.tree[node]


N = int(input())
arr = [*map(int, input().split())]
tree = SegmentTree([0] + arr, N)
M = int(input())
answer = []
for _ in range(M):
    v, a, b = map(int, input().split())
    if v == 1:
        tree.update(1, 1, N, a, b)
    if v == 2:
        answer.append(tree.calc(1, 1, N, a, b))
print(*answer, sep='\n')
