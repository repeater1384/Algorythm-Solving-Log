names = [input()[0] for _ in range(int(input()))]

answers=[]
for alpha in set(names):
    if names.count(alpha) >= 5:
        answers.append(alpha)

if answers:
    print(*sorted(answers),sep='')
else:
    print('PREDAJA')