n, s = map(int, input().split())
sequence = [*map(int, input().split())]

end = 0
current_sum = 0
answer = 0

for start in range(n):
    while end < n and current_sum < s:
        current_sum += sequence[end]
        end += 1

    if current_sum == s:
        answer += 1
    current_sum -= sequence[start]

print(answer)
