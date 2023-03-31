from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
start = ''.join([input().replace(' ', '') for _ in range(3)])
visited = {start: 0}
queue = deque()
queue.append((start, 0))

answer = -1
while queue:
    cur, cnt = queue.popleft()
    if cur == '123456780':
        answer = cnt
        break
    empty = cur.index('0')
    cy, cx = divmod(empty, 3)

    for k in range(4):
        ny, nx = cy + dy[k], cx + dx[k]
        if 0 <= ny < 3 and 0 <= nx < 3:
            swap = ny * 3 + nx
            next = list(cur)
            next[swap], next[empty] = next[empty], next[swap]
            next = ''.join(next)
            
            if next not in visited:
                visited[next] = cnt + 1
                queue.append((next, cnt + 1))
print(answer)
