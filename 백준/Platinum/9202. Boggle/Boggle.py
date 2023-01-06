import sys


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False


def insert(root, word):
    cur = root
    for w in word:
        if w not in cur.children:
            cur.children[w] = Trie()
        cur = cur.children[w]
    cur.is_end = True


def travel(cur, prefix):
    for key in cur.children.keys():
        travel(cur.children[key], prefix + '--')


def find(root, word):
    cur = root
    for w in word:
        if w not in cur.children:
            return False
        cur = cur.children[w]
    return cur.is_end


di, dj = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]


def backtracking(i, j, matrix, visited, make, cur, depth):
    global finded
    if find(root, make):
        finded.add(make)
    if depth == 8:
        return

    for k in range(8):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4 and not visited[ni][nj]:
            visited[ni][nj] = True
            if matrix[ni][nj] in cur.children:
                backtracking(ni, nj, matrix, visited, make + matrix[ni][nj], cur.children[matrix[ni][nj]], depth + 1)
            visited[ni][nj] = False


input = sys.stdin.readline

score_board = [0, 0, 0, 1, 1, 2, 3, 5, 11]
N = int(input().rstrip())

root = Trie()
words = [input().rstrip() for _ in range(N)]
for word in words:
    insert(root, word)
input()
M = int(input())

for m in range(M):
    matrix = [[*input().rstrip()] for _ in range(4)]
    finded = set()
    visited = [[False] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if matrix[i][j] in root.children:
                visited[i][j] = True
                backtracking(i, j, matrix, visited, matrix[i][j], root.children[matrix[i][j]],1)
                visited[i][j] = False
    score = 0
    for find1 in finded:
        score += score_board[len(find1)]
    longest_word = sorted(finded, key=lambda x: (-len(x), x))[0]
    print(score, longest_word, len(finded))
    if m < M - 1:
        input()
