import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

N = int(input())
nodes = [[-1, -1] for _ in range(N + 1)]
is_root = [True] * (N + 2)
for _ in range(N):
    me, left, right = map(int, input().split())
    is_root[left] = False
    is_root[right] = False
    nodes[me][0] = left
    nodes[me][1] = right

cur_width = 1
max_height = -1
height_list = [[] for _ in range(N + 1)]


def inorder(cur, height):
    global cur_width, max_height
    max_height = max(max_height, height)
    if nodes[cur][0] != -1:
        inorder(nodes[cur][0], height + 1)
    height_list[height].append(cur_width)
    cur_width += 1
    if nodes[cur][1] != -1:
        inorder(nodes[cur][1], height + 1)
        

inorder(is_root[1:-1].index(True) + 1, 1)
answer_width = -1
answer_height = -1
for level in range(1, max_height + 1):
    max_width_diff = height_list[level][-1] - height_list[level][0] + 1
    if answer_width < max_width_diff:
        answer_width = max_width_diff
        answer_height = level
print(answer_height, answer_width)
