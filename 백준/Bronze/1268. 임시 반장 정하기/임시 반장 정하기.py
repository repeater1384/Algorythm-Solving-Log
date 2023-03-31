N = int(input())

matrix = [[*map(int, input().split())] for _ in range(N)]
data = {i: set() for i in range(1, N + 1)}

for t in zip(*matrix):
    freq = {}
    for idx, i in enumerate(t):
        if freq.get(i) is None:
            freq[i] = [idx + 1]
        else:
            freq[i].append(idx + 1)

    for k, v in freq.items():
        temp = set(v)
        for s in v:
            for a in temp - {s}:
                data[s].add(a)

max_friend = 0
answer = 1
for k, v in data.items():
    if max_friend < len(v):
        answer = k
        max_friend = len(v)

print(answer)
