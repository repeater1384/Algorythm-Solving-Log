n = input()
if '0' not in n or sum([int(i) for i in n]) % 3 != 0:
    print(-1)
else:
    n = ''.join(sorted(list(n),reverse=True))
    print(n)