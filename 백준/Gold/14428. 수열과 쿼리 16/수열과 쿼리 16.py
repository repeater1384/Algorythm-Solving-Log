import sys

input = sys.stdin.readline


class SegmentTree:
    def __init__(self, arr, N):
        self.arr = arr
        self.tree = [0] * (N * 4)
        self.init_tree(1, 1, N)

    def init_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start], start
        else:
            mid = (start + end) // 2
            left, left_idx = self.init_tree(node * 2, start, mid)
            right, right_idx = self.init_tree(node * 2 + 1, mid + 1, end)
            if right < left:
                self.tree[node] = right, right_idx
            else:
                self.tree[node] = left, left_idx
        return self.tree[node]

    def calc(self, node, start, end, left, right):
        # [left, right] 구간을 구함. left, right는 고정
        if right < start or end < left:
            return float('inf'), float('inf')
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2

        temp1, temp1_idx = self.calc(node * 2, start, mid, left, right)
        temp2, temp2_idx = self.calc(node * 2 + 1, mid + 1, end, left, right)
        if temp2 < temp1:
            return temp2, temp2_idx
        return temp1, temp1_idx

    def update(self, node, start, end, new_idx, new_val):
        # new_idx의 값을 new_val로 바꿈, new_idx, new_val 고정
        if new_idx < start or end < new_idx:
            pass
        elif start == end:
            self.tree[node] = new_val, new_idx
        else:
            mid = (start + end) // 2
            temp1, temp1_idx = self.update(node * 2, start, mid, new_idx, new_val)
            temp2, temp2_idx = self.update(node * 2 + 1, mid + 1, end, new_idx, new_val)
            if temp2 < temp1:
                self.tree[node] = temp2, temp2_idx
            else:
                self.tree[node] = temp1, temp1_idx
        return self.tree[node]


N = int(input())
arr = [0] + [*map(int, input().split())]
tree = SegmentTree(arr, N)
M = int(input())
answer = []
for _ in range(M):
    v, a, b = map(int, input().split())
    if v == 1:
        tree.update(1, 1, N, a, b)
    if v == 2:
        answer.append(tree.calc(1, 1, N, a, b)[1])
print(*answer, sep='\n')
