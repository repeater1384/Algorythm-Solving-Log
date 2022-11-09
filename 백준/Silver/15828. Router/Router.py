import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
buffer = int(input())

while True:
    N = int(input())
    if N == -1:
        break
    if N == 0:
        queue.popleft()
    else:
        if len(queue) < buffer:
            queue.append(N)

if queue:
    print(*queue)
else:
    print('empty')