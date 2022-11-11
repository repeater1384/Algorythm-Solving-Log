import sys

input = sys.stdin.readline

lines = sorted([sorted(map(int, input().split())) for _ in range(int(input()))], key=lambda x: x[0])
answer = 0
left, right = lines[0][0], lines[0][1]

for i in range(len(lines)):
    if right < lines[i][0]:
        answer += right - left
        left = lines[i][0]
        right = lines[i][1]
    else:
        right = max(right, lines[i][1])

answer += right - left

print(answer)
