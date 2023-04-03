from collections import deque

N = 5
matrix = [[*input()] for _ in range(N)]
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
answer = 0


def comb(start, selected):
    global answer
    if len(selected) == 7:
        # 모두 인접하고, 이다솜파가 네명 이상이여야함.
        som_cnt = sum([1 if matrix[i][j] == 'S' else 0 for i, j in selected])
        if not som_cnt >= 4:
            return

        queue = deque()
        si, sj = selected[0]
        queue.append((si, sj))
        visited = [[False] * N for _ in range(N)]
        visited[si][sj] = True
        
        while queue:
            i, j = queue.popleft()
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if not visited[ni][nj] and (ni, nj) in selected:
                        queue.append((ni, nj))
                        visited[ni][nj] = True
                        
        for i, j in selected:
            if not visited[i][j]:
                return
        answer += 1
        
    for i in range(start, N * N):
        comb(i + 1, selected + [(i // 5, i % 5)])


comb(0, [])
print(answer)
