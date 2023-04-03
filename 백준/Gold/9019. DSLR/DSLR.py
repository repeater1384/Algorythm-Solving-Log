from collections import deque
import sys

input = sys.stdin.readline


def bfs(a, b):
    # def D(n):
    #     return n * 2 % 10000
    #
    # def S(n):
    #     return n - 1 if n != 0 else 9999
    #
    # def L(n):
    #     return (n * 10 + n // 1000) % 10000
    #
    # def R(n):
    #     return (n + (n % 10) * 10000) // 10

    queue = deque()
    queue.append((a, ''))
    visited = [False] * 10000
    visited[a] = True
    while queue:
        cur, res = queue.popleft()
        if cur == b:
            return res
        d = cur * 2 % 10000
        s = cur - 1 if cur != 0 else 9999
        l = (cur * 10 + cur // 1000) % 10000
        r = (cur + (cur % 10) * 10000) // 10
        for temp1, temp2 in zip([d, s, l, r], ['D', 'S', 'L', 'R']):
            if not visited[temp1]:
                queue.append((temp1, res + temp2))
                visited[temp1] = True


for _ in range(int(input())):
    A, B = map(int, input().split())
    print(bfs(A, B))
