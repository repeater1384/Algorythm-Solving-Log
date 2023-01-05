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


def check(root, word):
    cnt = 1
    cur = root.children[word[0]]
    for w in word[1:]:
        if cur.is_end or len(cur.children.keys()) > 1:
            cnt += 1
        cur = cur.children[w]
    return cnt


while True:
    try:
        N = int(input())
    except EOFError:
        break

    root = Trie()
    words = [input() for _ in range(N)]
    for word in words:
        insert(root, word)
    avg = 0
    for word in words:
        cnt = check(root, word)
        avg += cnt
    print(f'{(avg / N):.2f}')
