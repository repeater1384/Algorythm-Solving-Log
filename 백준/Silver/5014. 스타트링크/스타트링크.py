from collections import deque

F, S, G, U, D = map(int, input().split())
queue = deque()
queue.append((S, 0))
visited = [False] * (F + 1)
visited[S] = True

answer = -1
while queue:
    cur, cnt = queue.popleft()
    if cur == G:
        answer = cnt
        break
    if cur - D >= 1 and not visited[cur - D]:
        queue.append((cur - D, cnt + 1))
        visited[cur - D] = True
    if cur + U <= F and not visited[cur + U]:
        queue.append((cur + U, cnt + 1))
        visited[cur + U] = True

print('use the stairs' if answer == -1 else answer)
