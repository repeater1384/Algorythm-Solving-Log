S = [*input()]
N = len(S)

for i in range(N - 1):
    j = i + 1
    if S[i] > S[j] and S[0] >= S[j]:
        S = S[:i + 1][::-1] + S[i + 1:]
        S = S[:i + 2][::-1] + S[i + 2:]
print(''.join(S))