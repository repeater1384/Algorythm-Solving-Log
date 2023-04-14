N, M = map(int, input().split())
balls = [i for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    balls[a], balls[b] = balls[b], balls[a]
print(*balls[1:])
