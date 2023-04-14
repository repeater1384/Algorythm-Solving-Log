data = input() + 'ILOVEYONSEI'
cur = data[0]
answer = 0
for c in data[1:]:
    answer += abs(ord(c) - ord(cur))
    cur = c
print(answer)
