import sys

N, M, K = map(int, input().split())
matrix = [[*sys.stdin.readline().rstrip()] for _ in range(N)]
ps = [[0] * (M + 1) for _ in range(N + 1)]

# ps[i][j] =>B로 시작하는 체스판으로 다시 칠할때 0,0부터 i,j까지 다시 칠해야 하는 판의 최솟값.
# B로 시작하는 체스판에서 바꿔야 하는 개수 = X
# W로 시작하는 체스판에서 바꿔야 하는 개수 = Y
# NM - X = Y 이므로, W로 시작하는건 따로 안세줘도 됨.
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if matrix[i - 1][j - 1] == ['B', 'W'][(i + j) % 2]:
            ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]
        else:
            ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + 1

# (i,j)는 누적합의 우측하단.
answer = float('inf')
for i in range(K, N + 1):
    for j in range(K, M + 1):
        cur = ps[i][j] - ps[i - K][j] - ps[i][j - K] + ps[i - K][j - K]
        answer = min(answer, cur, K * K - cur)
print(answer)
