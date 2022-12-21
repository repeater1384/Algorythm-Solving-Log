N, M = map(int, input().split())

arr = [[*input()] for _ in range(N)]
answer = ''
distance = 0
for col in zip(*arr):
    freq = {c: 0 for c in ['T', 'A', 'G', 'C']}
    for c in col:
        freq[c] += 1
    max_freq = max(freq.values())
    for c in ['A', 'C', 'G', 'T']:
        if freq[c] == max_freq:
            answer += c
            distance += N - max_freq
            break

print(answer)
print(distance)
