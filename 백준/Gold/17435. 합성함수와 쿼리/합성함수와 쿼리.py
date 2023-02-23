import sys

input = sys.stdin.readline

M = int(input())
arr = [*map(int, input().split())]
LOG = 20
# sparse_matrix[i][x] ==> f^i(x)
sparse_matrix = [[-1] * (M + 1) for _ in range(LOG)]


def make():
    sparse_matrix[0] = [0] + arr
    for i in range(1, LOG):
        for x in range(1, M + 1):
            sparse_matrix[i][x] = sparse_matrix[i - 1][sparse_matrix[i - 1][x]]


make()
Q = int(input())
answer = []
for _ in range(Q):
    n, x = map(int, input().split())
    cur = x
    for i in range(LOG - 1, -1, -1):
        if n & (1 << i):
            cur = sparse_matrix[i][cur]
    answer.append(str(cur))
print('\n'.join(answer))
