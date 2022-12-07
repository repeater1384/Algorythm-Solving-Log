import sys

input = sys.stdin.readline


class SegmentTree:
    def __init__(self, arr, N):
        self.arr = arr
        self.tree = [0] * (N * 4)
        self.lazy = [0] * (N * 4)
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
        self.propagate(node, start, end)
        # [left, right] 구간을 구함. left, right는 고정
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        temp1 = self.query(node * 2, start, mid, left, right)
        temp2 = self.query(node * 2 + 1, mid + 1, end, left, right)
        return temp1 + temp2

    def update_range(self, node, start, end, left, right, added):
        self.propagate(node, start, end)
        # [left, right] 구간에 added를 더함, (left, right, added)는 고정
        if right < start or end < left:
            # 완전히 벗어나면 안해도됨
            pass
        elif left <= start and end <= right:
            # 완전히 포함된다면, tree에 반영하고, 자식한테 lazy만 전달
            self.tree[node] += (end - start + 1) * added
            if start != end:
                self.lazy[node * 2] += added
                self.lazy[node * 2 + 1] += added
        else:
            # 걸쳐있으면 재귀적으로 수행.
            mid = (start + end) // 2
            temp1 = self.update_range(node * 2, start, mid, left, right, added)
            temp2 = self.update_range(node * 2 + 1, mid + 1, end, left, right, added)
            self.tree[node] = temp1 + temp2
        return self.tree[node]

    def propagate(self, node, start, end):
        # 이 함수는 update, query 함수가 호출될때마다 먼저 실행될거임
        # staet, end 범위 내려가면서 알아서 호출되니까 여기선 단순반영만 하자
        # lazy값 반영하는 부분 갱신할 값 없으면 자식도 없는 거니까 return
        if self.lazy[node] == 0:
            return

        # 아까 반영 안하고 더해만 놓았던 added 반영하는 부분
        self.tree[node] += (end - start + 1) * self.lazy[node]
        if start != end:
            self.lazy[node * 2] += self.lazy[node]
            self.lazy[node * 2 + 1] += self.lazy[node]
        # 처리 한 다음엔 0으로 초기화
        self.lazy[node] = 0


N = int(input())
arr = [0] + [*map(int, input().split())]
tree = SegmentTree(arr, N)

answer = []
M = int(input())
for _ in range(M):
    v, *info = map(int, input().split())
    if v == 1:
        a, b, c = info
        tree.update_range(1, 1, N, a, b, c)
    if v == 2:
        a = info[0]
        answer.append(tree.query(1, 1, N, a, a))
print(*answer, sep='\n')
