INF = int(1e9)


def bf(start):
    # 벨만포드 알고리즘 응용, 음수사이클 존재여부 리턴
    distance = [INF] * (N + 1)
    distance[start] = 0

    for time in range(N):
        for edge in edges:
            a, b, w = edge
            if distance[a] > distance[b] + w:
                distance[a] = distance[b] + w
                if time == N - 1:
                    return True
    return False


TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, w = map(int, input().split())
        edges.append((a, b, w))
        edges.append((b, a, w))
    for _ in range(W):
        a, b, w = map(int, input().split())
        edges.append((a, b, -w))

    cycle = bf(1)
    print('YES' if cycle else 'NO')
