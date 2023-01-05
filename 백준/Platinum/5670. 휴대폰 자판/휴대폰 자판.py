import sys

input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.children_num = 0
        self.is_end = False


def ctoi(c):
    return ord(c) - ord('a')


def insert(root, word):
    cur = root
    for w in map(lambda x: ctoi(x), word):
        if not cur.children[w]:
            cur.children[w] = Trie()
            cur.children_num += 1
        cur = cur.children[w]
    cur.is_end = True


def check(root, word):
    cnt = 1
    cur = root.children[ctoi(word[0])]
    for w in [*map(lambda x: ctoi(x), word)][1:]:
        if cur.is_end or cur.children_num > 1:
            cnt += 1
        cur = cur.children[w]
    return cnt


while True:
    try:
        N = int(input().strip())
    except:
        break

    root = Trie()
    words = [input().strip() for _ in range(N)]
    for word in words:
        insert(root, word)

    temp = [check(root, word) for word in words]
    avg = sum(temp) / N
    print(f'{avg:.2f}')
