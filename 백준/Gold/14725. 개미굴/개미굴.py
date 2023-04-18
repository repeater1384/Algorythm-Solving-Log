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
    for key in sorted(cur.children.keys()):
        print(prefix + key)
        travel(cur.children[key], prefix + '--')


N = int(input())
root = Trie()
for _ in range(N):
    arr = [*input().split()][1:]
    insert(root, arr)

travel(root, '')
