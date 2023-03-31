import sys
read = lambda : sys.stdin.readline().strip()
sys.setrecursionlimit(10000)
def printboard(matrix):
    for a in matrix:
        print(a)
    print()
def dfs(matrix, x,y):
    matrix[y][x]=0
    # 이건 이제 이미 간것이다. 하고 0으로 바꾸는것 이다.
    h = len(matrix)
    w = len(matrix[0])
    dx = [1,-1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    for i in range(8):
        n_x = x + dx[i]
        n_y = y + dy[i]
        # 이 근처 다 n_x, n_y로 간다.
        if n_x>=0 and n_x<w and n_y>=0 and n_y<h:
            # 범위 check
            if matrix[n_y][n_x]==1:
            # 그부분이 1이면
                dfs(matrix, n_x, n_y)
                # cnt를 증가시켜서 다시한번 그 근처 확인
    return
    # 다 cnt검사하면 끝을 낸다.

while True:
    w,h = map(int,input().split())
    if w+h == 0:
        break
    matrix = [[*map(int,input().split())] for _ in range(h)]
    ans = 0
    for y in range(h):
        for x in range(w):
            if matrix[y][x]==1:
                dfs(matrix,x,y)
                ans +=1
    print(ans)