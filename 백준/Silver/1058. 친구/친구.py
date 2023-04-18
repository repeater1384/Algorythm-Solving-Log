N = int(input())
matrix = [[*input()] for _ in range(N)]
friend_set = [set() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'Y':
            friend_set[i].add(j)

answer = 0
for i in range(N):
    cur = set(friend_set[i])
    for c in friend_set[i]:
        cur |= friend_set[c]
    answer = max(answer, len(cur - {i}))
print(answer)
