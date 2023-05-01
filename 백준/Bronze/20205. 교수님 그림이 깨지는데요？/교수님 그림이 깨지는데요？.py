N, K = map(int, input().split())

matrix = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    for _ in range(K):
        for j in range(N):
            print((str(matrix[i][j])+' ')*K,end='')
        print()

