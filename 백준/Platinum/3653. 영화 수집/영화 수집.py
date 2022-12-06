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
            self.tree[node] = left + right
        return self.tree[node]

    def query(self, node, start, end, left, right):
        # [left, right] 구간을 구함. left, right는 고정
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        temp1 = self.query(node * 2, start, mid, left, right)
        temp2 = self.query(node * 2 + 1, mid + 1, end, left, right)
        return temp1 + temp2

    def update(self, node, start, end, idx, new_val):
        # idx의 값을 new_val로 바꾸고 트리를 업데이트함
        if end < idx or idx < start:
            pass
        elif start == end:
            self.tree[node] = new_val
        else:
            mid = (start + end) // 2
            temp1 = self.update(node * 2, start, mid, idx, new_val)
            temp2 = self.update(node * 2 + 1, mid + 1, end, idx, new_val)
            self.tree[node] = temp1 + temp2
        return self.tree[node]


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [1] * (N + 1) + [0] * M
    dvd_idx = {N + 1 - i: i for i in range(1, N + 1)}
    tree = SegmentTree(arr, N + M)
    answer = []
    new_idx = N
    for dvd_num in map(int, input().split()):
        idx = dvd_idx[dvd_num]
        answer.append(tree.query(1, 1, N + M, idx + 1, new_idx))
        tree.update(1, 1, N + M, idx, 0)
        new_idx += 1
        tree.update(1, 1, N + M, new_idx, 1)
        dvd_idx[dvd_num] = new_idx

    print(*answer)
