score = input()
N = len(score)
a = sum(map(int, score[:N // 2]))
b = sum(map(int, score[N // 2:]))
print('LUCKY' if a == b else 'READY')
