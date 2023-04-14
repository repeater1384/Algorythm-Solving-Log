N, M = map(int, input().split())
check = [False] * (N + 1)
answer = [0] * M


def dfs(index, n, m):
    if index == m:
        print(' '.join(answer))

    else:
        for i in range(1, n + 1):
            if check[i]:
                continue

            check[i] = True
            answer[index] = str(i)
            dfs(index + 1, n, m)
            check[i] = False


dfs(0, N, M)
