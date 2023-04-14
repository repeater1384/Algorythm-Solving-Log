class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False


def search(root, word):
    cur = root
    for w in word:
        if cur.is_end:
            return False
        cur = cur.children[w]
    return True


def insert(root, word):
    cur = root
    for w in word:
        if w not in cur.children:
            cur.children[w] = Trie()
        cur = cur.children[w]
    cur.is_end = True


T = int(input())
for _ in range(T):
    N = int(input())
    root = Trie()
    arr = [input() for _ in range(N)]
    for data in arr:
        insert(root, data)
    answer = True
    for data in arr:
        if not search(root, data):
            answer = False
            break
    print('YES' if answer else 'NO')
