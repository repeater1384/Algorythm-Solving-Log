h,w = map(int,input().split())
matrix = [[*map(int,list(input()))] for _ in range(h)]
dist = [[0] * w for _ in range(h)]
check = [[False] * w for _ in range(h)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = [(0,0)]
check[0][0] = True
dist[0][0] =1

while q:
    x,y = q.pop(0)
    check[y][x] = True
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if nx>=0 and nx<w and ny>=0 and ny<h:
            if not check[ny][nx] and matrix[ny][nx] == 1:
                q.append((nx,ny))
                dist[ny][nx] = dist[y][x] + 1
                check[ny][nx] = True

print(dist[h-1][w-1])