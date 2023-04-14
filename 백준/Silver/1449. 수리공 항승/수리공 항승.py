N, L = map(int, input().split())
holes = sorted([*map(int, input().split())])

answer = 1

s, e = holes[0], holes[0] + L

for idx in range(N):
    if s <= holes[idx] < e:
        continue
    s, e = holes[idx], holes[idx] + L
    answer += 1

print(answer)
