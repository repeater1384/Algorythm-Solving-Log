from collections import deque

N, K = map(int, input().split())

queue = deque([(N, 0)])
visited = [False] * 100001

answer = 0
route = 0
find_answer = False

while queue:
    cur, cnt = queue.popleft()
    visited[cur] = True

    if find_answer and cnt > answer:
        break

    if cur == K:
        if not find_answer:
            answer = cnt
            find_answer = True
        route += 1

    if cur - 1 >= 0 and not visited[cur - 1]:
        queue.append((cur - 1, cnt + 1))

    if cur + 1 <= 100000 and not visited[cur + 1]:
        queue.append((cur + 1, cnt + 1))

    if cur * 2 <= 100000 and not visited[cur * 2]:
        queue.append((cur * 2, cnt + 1))

print(answer)
print(route)