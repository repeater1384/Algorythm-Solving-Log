from collections import deque

N = int(input())
adj_matrix = [[False] * (N + 1) for _ in range(N + 1)]
INF = float('inf')
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    adj_matrix[a][b] = True
    adj_matrix[b][a] = True


def calc_score(num):
    queue = deque()
    friend = [INF] * (N + 1)
    queue.append((num, 0))
    friend[num] = 0
    while queue:
        cur, friendly = queue.popleft()
        for next in range(1, N + 1):
            if adj_matrix[cur][next] and friend[next] == INF:
                friend[next] = friendly + 1
                queue.append((next, friendly + 1))
    return max(friend[1:])


score_list = [calc_score(i) for i in range(N + 1)]
print(min(score_list), score_list.count(min(score_list)))
print(*[num for num, score in enumerate(score_list) if score == min(score_list)])
