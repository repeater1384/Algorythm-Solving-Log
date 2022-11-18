N = int(input())
data = [[*map(int, input().split())] for _ in range(N)]
data.sort(key=lambda x: x[0])

left = [data[0]]
right = [data[-1]]
# fill left
for cur in data[1:]:
    if cur[1] >= left[-1][1]:
        left.append(cur)
# fill right
for cur in data[::-1][1:]:
    if cur[1] > right[-1][1]:
        right.append(cur)

if left[-1] == right[-1]:
    answer = left[-1][1]
    for i in range(len(left) - 1):
        answer += (left[i + 1][0] - left[i][0]) * left[i][1]
    for i in range(len(right) - 1):
        answer += (right[i][0] - right[i + 1][0]) * right[i][1]
    print(answer)
else:
    answer = left[-1][1] * (right[-1][0]-left[-1][0])
    print(answer)
