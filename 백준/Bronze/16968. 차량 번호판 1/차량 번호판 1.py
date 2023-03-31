fmt = input()
answer = 1

idx = 0
d = 10
c = 26

while idx < len(fmt):
    if fmt[idx] == 'c':
        answer *= c
        d = 10
        c = max(25, c - 1)
    else:
        answer *= d
        c = 26
        d = max(9, d - 1)
    idx += 1

print(answer)
