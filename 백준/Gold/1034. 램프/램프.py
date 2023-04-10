N, M = map(int, input().split())
matrix = [input() for _ in range(N)]
K = int(input())

freq = {}
for row in matrix:
    if row in freq:
        freq[row] += 1
    else:
        freq[row] = 1

answer = 0
for row, cnt in freq.items():
    zero = row.count('0')
    if zero <= K and (K - zero) % 2 == 0:
        answer = max(answer, cnt)
print(answer)
