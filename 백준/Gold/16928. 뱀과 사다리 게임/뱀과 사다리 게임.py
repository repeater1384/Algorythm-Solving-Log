from collections import deque

N, M = map(int, input().split())
move = {}
for _ in range(N + M):
    x, y = map(int, input().split())
    move[x] = y

visited = [0] * 101

queue = deque([(1, 0)])  # (현재 위치, 현재 위치까지 이동할때 걸리는 주사위 횟수의 최솟값)
visited[1] = 1

while queue:
    cur, cnt = queue.popleft()
    if cur == 100:
        answer = cnt
        break

    for i in range(1, 7):  # i > 주사위 눈금
        new = cur + i
        if new > 100: break
        if visited[new]: continue

        if move.get(new):
            new = move[new]

        visited[new] = 1
        queue.append((new, cnt + 1))

print(answer)
