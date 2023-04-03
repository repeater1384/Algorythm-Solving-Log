A, B, C = map(int, input().split())

answer = set()

check = [[[False] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)]


def dfs(a, b, c):
    if check[a][b][c]:
        return
    check[a][b][c] = True
    if a == 0:
        answer.add(c)

    # b에서 a로 주기
    if a + b <= A:
        dfs(a + b, 0, c)
    else:
        dfs(A, a + b - A, c)

    # c에서 a로 주기
    if a + c <= A:
        dfs(a + c, b, 0)
    else:
        dfs(A, b, a + c - A)

    # a에서 b로 주기
    if a + b <= B:
        dfs(0, a + b, c)
    else:
        dfs(a + b - B, B, c)

    # c에서 b로 주기
    if b + c <= B:
        dfs(a, b + c, 0)
    else:
        dfs(a, B, b + c - B)

    # a에서 c로 주기
    if a + c <= C:
        dfs(0, b, a + c)
    else:
        dfs(a + c - C, b, C)

    # b에서 c로 주기
    if b + c <= C:
        dfs(a, 0, b + c)
    else:
        dfs(a, b + c - C, C)

dfs(0,0,C)
print(*sorted(answer))
