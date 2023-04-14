expression = input()
temp = expression.split('-')
answer = 0
for a in temp[0].split('+'):
    answer += int(a)

for a in temp[1:]:
    for b in a.split('+'):
        answer -= int(b)
print(answer)
